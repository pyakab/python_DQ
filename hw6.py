from datetime import date, datetime
import os
import os.path

current_date = datetime.today()


class Publication:
    def __init__(self, text):
        self.text = text

    def publishing(self):
        return f"{self.text}"


class News(Publication):
    def __init__(self, text, city):
        Publication.__init__(self, text)
        self.city = city

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
            text_file.write(
                f"\n\nPrivate ad------------\n{self.text} \nActual until: {self.expiration_date}, {ndays} days left.")


class BlogPost(Publication):
    def __init__(self, text, title, author, tag):
        Publication.__init__(self, text)
        self.title = title
        self.author = author
        self.tag = tag

    def publishing_post(self):
        print(self.text)
        with open("news_feed.txt", "a") as text_file:
            text_file.write(
                f"\n\nBlog post------------\n {self.title} \n Author: {self.author} \n {self.text} \n tag: {self.tag}")


class FileUpload(Publication):
    def __init__(self, filepath):
        self.filepath = filepath

    def publishing_from_file(self):
        # with open(self.filepath, 'r') as f:
        #    filetext = f.read()
        # print(filetext)
        with open(self.filepath) as f:
            for line in f:
                line = line.lower()
                if line.startswith('news'):
                    city = next(f).strip()
                    print(city)
                    if city != '':
                        text = next(f).strip()
                        print(text)
                        new_news = News(text, city)
                        new_news.publishing_news()
                    else:
                        print('File has the wrong format')
                        break

                if line.startswith('private ad'):
                    deadline_date = next(f).strip()
                    try:
                        expiration_date = datetime.strptime(deadline_date, '%Y/%m/%d')
                    except:
                        print(
                            'Wrong date format!\nPlease repeat the input of ad with the right date format(yyyy/mm/dd)')
                        break
                    if (expiration_date - current_date).days < 0:
                        print(
                        f'Wrong date was input - {deadline_date}\n'
                        f'Please repeat the input of ad with the right date (later than today)')
                        break
                    if deadline_date != '':
                        text = next(f).strip()
                        new_private_ad = PrivateAd(text, expiration_date)
                        new_private_ad.publishing_ad()
                    else:
                        print('File has the wrong format')

            if line.startswith('blog post'):
                title = next(f).strip()
                if title != '':
                    author = next(f).strip()
                    if author != '':
                        text = next(f).strip()
                        if text != '':
                            tag = next(f).strip()
                            new_blogpost = BlogPost(text, title, author, tag)
                            new_blogpost.publishing_post()
                            upload_to_print = FileUpload(filepath)
                            upload_to_print.delete_file()

                else:
                    print('Text have the wrong format')

        # with open("news_feed.txt", "a") as text_file:
        #    text_file.write(f"\n\n{filetext}")

    def delete_file(self):
        file_for_delete = self.filepath
        os.remove(file_for_delete)


class Normalization:

    def __init__(self):
        self.text_file = 'news_feed.txt'

    def normalizing_file(self):
        text_file = self.text_file
        with open(text_file, 'r') as f:
            text_file = f.read()
        text_file = text_file.lower()
        updated_file = []
        text_file1 = []
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
            elif updated_file[y - 2] == "\n" and updated_file[y - 1] == " ":
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
        if os.path.exists("normalized_newsfeed.txt"):
            os.remove("normalized_newsfeed.txt")
        else:
            print('File isn`t found')
        with open("normalized_newsfeed.txt", "a") as text_file:
            text_file.write(f"{final_formatted_text}")


class Main:
    y = 0
    while y == 0:
        print('Do you want to add text from file or input it with keyboard? (Options: file / keyboard)')
        inputway = input()
        print(f'Your answer is:\n{inputway}')
        if inputway.lower() == 'keyboard':
            print('What type of publication do you want to add? (Options: news / private ad / blog post)')
            answer = input()
            print(f'Your answer is:\n{answer}')
            if answer.lower() == 'news':
                print('What city was happened news in?')
                city = input()
                print('Print the text of the news')
                text = input()
                # print('Input the filepath:')
                # filepath = input()
                # print(f'Your answer is:\n{filepath}')
                # upload_to_print = FileUpload(filepath)
                # upload_to_print.publishing_from_file()
                new_news = News(text, city)
                new_news.publishing_news()
            elif answer.lower() == 'private ad':
                print('When is the deadline of this ad? (yyyy/mm/dd)')
                deadline_date = input()
                try:
                    expiration_date = datetime.strptime(deadline_date, '%Y/%m/%d')
                except:
                    print('Wrong date format!\nPlease repeat the input of ad with the right date format(yyyy/mm/dd)')
                    break  # out of program
                if (expiration_date - current_date).days < 0:
                    print(
                        f'Wrong date was input - {deadline_date}\n'
                        f'Please repeat the input of ad with the right date (later than today)')
                    break
                else:
                    pass
                print(expiration_date)
                print('Print the text of the ad')
                text = input()
                new_private_ad = PrivateAd(text, expiration_date)
                new_private_ad.publishing_ad()
            elif answer.lower() == 'blog post':
                print('What is a title of post?')
                title = input()
                print('Who is an author of this post?')
                author = input()
                print('Print the text of the post')
                text = input()
                print('What tag do you want to add to this post')
                tag = input()
                new_blogpost = BlogPost(text, title, author, tag)
                new_blogpost.publishing_post()
            else:
                print('This type of publication can`t be added to the news feed')

        elif inputway == 'file':
            cwd = os.getcwd()
            print(cwd)
            print(
                f'Provide the name of your file in the directory {cwd}'
                f' or the filepath to the file in the another directory :')
            fileinput = input()
            print(f'Your answer is:\n{fileinput}')
            inputfilepath = os.path.join(cwd, fileinput)
            print(inputfilepath)
            if os.path.isfile(inputfilepath):
                filepath = inputfilepath
                print('Exists')
                upload_to_print = FileUpload(filepath)
                upload_to_print.publishing_from_file()
                upload_to_print.delete_file()

            elif os.path.isfile(fileinput):
                filepath = fileinput
                print('Another directory')
                upload_to_print = FileUpload(filepath)
                upload_to_print.publishing_from_file()
                upload_to_print.delete_file()
            else:
                print('Not exist')
                break

        print('Do you want to add another publication? (Options: y/n)')
        another_publication = input()
        if another_publication == 'y':
            y = 0
        else:
            y = 1


normal_file = Normalization()  # 'normalization' object is not callable error when second publication is done;
# use another name for variable

normal_file.normalizing_file()

if __name__ == "__main__":
    Main()

# To correct:
# Write from file: should define type of publication (by user or read from file) and
# write to output file according to the rules. For example,
# if News - current day and time should be added;
# You can specify in what format you expect the records in file. For
# example:
# Line1: type of publication (if you decide that not defined by user but read from file)
# Line 2: text
# Line 3: city or date (depending on line 1)
# Line 4: empty
# Line 5: type of publication etc.
# Process line by line. If some error - do not add records to file
# and do not delete the file.

# Minor mistakes, correct if time permits:
# 1.Define your input format (one or many records) - not done. You can make realization for
# writing only 1 publication from file, it will be ok
#
# 2.Default folder or user provided file path  (for output path) - not done

# PEP 8 standard:
# if another_publication=='y': -> if another_publication == 'y': (spaces before and after ==) ++
# new_private_ad = PrivateAd(text,expiration_date) -> new_private_ad = PrivateAd(text, expiration_date) - space after "text, " ++
# text_file=self.text_file ->  text_file = self.text_file - space before and after = +