from datetime import date, datetime
import os
import csv

current_date = datetime.today()

class Publication():
    def __init__(self, text):
        self.text = text

    def publishing(self):
        return f"{self.text}"

class News(Publication):
    def __init__(self, text, city):
        Publication.__init__(self, text)
        self.city=city


    def publishing_news(self):
        news_date = date.today()
        with open("news_feed.txt", "a") as text_file:
            text_file.write(f"\n\nNews------------\n {self.text}\n{self.city}, {news_date}")


class PrivateAd(Publication):
    def __init__(self, text, expiration_date):
        Publication.__init__(self, text)
        self.expiration_date = expiration_date


    def publishing_ad(self):
        ndays = (self.expiration_date - current_date).days
        with open("news_feed.txt", "a") as text_file:
            text_file.write(f"\n\nPrivate ad------------\n{self.text} \nActual until: {self.expiration_date}, {ndays} days left.")


class BlogPost(Publication):
    def __init__(self, text, title, author, tag):
        Publication.__init__(self, text)
        self.title = title
        self.author = author
        self.tag = tag

    def publishing_post(self):
        print(self.text)
        with open("news_feed.txt", "a") as text_file:
            text_file.write(f"\n\nBlog post------------\n {self.title} \n Author: {self.author} \n {self.text} \n tag: {self.tag}")

class FileUpload(Publication):
    def __init__(self, filepath):
        self.filepath = filepath


    def publishing_from_file(self):
        with open(self.filepath, 'r') as f:
            filetext = f.read()
        print(filetext)
        with open("news_feed.txt", "a") as text_file:
            text_file.write(f"\n\n{filetext}")



    def delete_file(self):
        file_for_delete=self.filepath
        os.remove(file_for_delete)

class Normalization():

    def __init__(self):
        self.text_file = 'news_feed.txt'


    def normalizing_file(self):
        text_file=self.text_file
        with open(text_file, 'r') as f:
            text_file = f.read()
        text_file=text_file.lower()
        updated_file=[]
        text_file1=[]
        x = 0
        while x < len(text_file):
            if text_file[x] == " " and text_file[x + 1] == " ":
                pass
            elif text_file[x] == " " and text_file[x + 1] == ".":
                pass
            elif text_file[x - 1] == "\n" and text_file[x] == "\t":
                pass
            elif text_file[x] == " " and text_file[x - 1] == "." and text_file[x + 1] == "\n":
                pass
            else:
                updated_file.append(text_file[x])
            x = x + 1

        y = 0
        while y < len(updated_file):
            if updated_file[y - 1] == "\n":
                text_file1.append(updated_file[y].upper())
            elif updated_file[y - 2]=="\n" and updated_file[y - 1]==" " :
                text_file1.append(updated_file[y].upper())
            elif updated_file[y - 2] == "." and updated_file[y - 1] == " ":
                text_file1.append(updated_file[y].upper())
            elif updated_file[y - 2] == "." and updated_file[y - 1] == "\n":
                text_file1.append(updated_file[y].upper())
            elif y == 0:
                text_file1.append(updated_file[y].upper())
            elif updated_file[y - 2] == ".":
                text_file1.append(updated_file[y].upper())
            elif updated_file[y - 2] == ":" and updated_file[y - 1] == "\n":
                text_file1.append(updated_file[y].upper())
            elif updated_file[y - 2] == ":" and updated_file[y - 1] == " ":
                text_file1.append(updated_file[y].upper())
            else:
                text_file1.append(updated_file[y])

            y = y + 1

        s1 = ""
        final_formatted_text = s1.join(text_file1)
        if (os.path.exists("normalized_newsfeed.txt")):
            os.remove("normalized_newsfeed.txt")
        else:
            print('File isn`t found')
        with open("normalized_newsfeed.txt", "a") as text_file:
            text_file.write(f"{final_formatted_text}")

        edited_file='normalized_newsfeed.txt'
        return edited_file

class FileCSV():
    def __init__(self):
        self.newsfeed="normalized_newsfeed.txt"

    def count_words(self):
        text = open(self.newsfeed, "rt")
        d = dict()
        for line in text:
            line = line.strip()
            line = line.lower()
            words = line.split(" ")

            for word in words:
                if word in d:
                    d[word] = d[word] + 1
                else:
                    d[word] = 1

        if (os.path.exists("word_stat.csv")):
            os.remove("word_stat.csv")
        else:
            print('File isn`t found')

        with open('word_stat.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            for k, v in d.items():
                writer.writerow([k, v])

    def show_statistics(self):
        infile = open(self.newsfeed, 'r')
        lines = 0
        words = 0
        characters = 0
        lower = 0
        upper = 0
        digits = 0
        whitespace = 0
        for line in infile:
            wordslist = line.split()
            lines = lines + 1
            words = words + len(wordslist)
            characters += sum(len(word) for word in wordslist)

        with open("normalized_newsfeed.txt") as file:
            #count = 0
            text = file.read()
            for i in text:
                if i.isupper():
                    upper += 1
                elif (i.isspace()):
                    whitespace += 1
                elif (i.islower()):
                    lower += 1
                elif (i.isdigit()):
                    digits += 1

        print(f"The number of characters is {characters}.")
        print(f"The number of uppercases is {upper}.")
        print(f"The number of whitespaces is {whitespace}.")


class main():
    y = 0
    while y==0 :
        print('Do you want to add text from file or input it with keyboard? (Options: file / keyboard)')
        inputway = input()
        print(f'Your answer is:\n{inputway}')
        if inputway.lower()=='keyboard':
            print('What type of publication do you want to add? (Options: news / private ad / blog post)')
            answer = input()
            print(f'Your answer is:\n{answer}')
            if answer.lower()=='news':
                print('What city was happened news in?')
                city = input()
                print('Print the text of the news')
                text = input()
                new_news = News(text,city)
                new_news.publishing_news()
            elif answer.lower()=='private ad':
                print('When is the deadline of this ad? (yyyy/mm/dd)')
                deadline_date = input()
                try:
                    expiration_date = datetime.strptime(deadline_date, '%Y/%m/%d')
                except:
                    print('Wrong date format!\nPlease repeat the input of ad with the right date format(yyyy/mm/dd)')
                    break
                if (expiration_date - current_date).days < 0:
                    print(f'Wrong date was input - {deadline_date}\nPlease repeat the input of ad with the right date (later than today)')
                    break
                else:
                    pass
                print(expiration_date)
                print('Print the text of the ad')
                text = input()
                new_private_ad = PrivateAd(text,expiration_date)
                new_private_ad.publishing_ad()
            elif answer.lower()=='private ad':
                print('When is the deadline of this ad?')
                expiration_date = input()
                print('Print the text of the ad')
                text = input()
                current_date = date.today()
                new_private_ad = PrivateAd(text,expiration_date)
                new_private_ad.publishing_ad()
            elif answer.lower()=='blog post':
                print('What is a title of post?')
                title = input()
                print('Who is an author of this post?')
                author = input()
                print('Print the text of the post')
                text = input()
                print('What tag do you want to add to this post')
                tag = input()
                new_blogpost = BlogPost(text,title, author, tag)
                new_blogpost.publishing_post()
            else:
                print('This type of publication can`t be added to the news feed')

        elif inputway=='file':
            print('Input the filepath:')
            filepath = input()
            print(f'Your answer is:\n{filepath}')
            upload_to_print=FileUpload(filepath)
            upload_to_print.publishing_from_file()
            upload_to_print.delete_file()


        print('Do you want to add another publication? (Options: y/n)')
        another_publication = input()
        if another_publication=='y':
            y = 0
        else:
            y = 1
        normalization = Normalization()
        newsfeed = normalization.normalizing_file()
        csv=FileCSV()
        csv.count_words()
        csv.show_statistics()


main()
