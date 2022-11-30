from datetime import date, datetime
import os
import os.path
import csv
import json
import xml.etree.ElementTree as ET
import sqlite3


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

    def __init__(self, filepath, text):
        super().__init__(text)
        self.filepath = filepath

    def publishing_from_file(self):
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
                            upload_to_print = FileUpload(self.filepath)
                            upload_to_print.delete_file()

                else:
                    print('Text have the wrong format')

    def delete_file(self):
        file_for_delete = self.filepath
        os.remove(file_for_delete)


class DBConnection:

    def select(self):

    def insert(self):

class JSONReading:

    def validateJSON(self, filepath):
        try:
            json.loads(filepath)
        except ValueError as err:
            return False
        return True

    def read_jsonfile(self):
        with open(self.filepath, 'r') as json_file:
            publication_data = json.load(json_file)
            print(publication_data)
            if (publication_data['type']) == 'news':
                print('It`s news')
                city = publication_data['city']
                text = publication_data['text']
                new_news = News(text, city)
                new_news.publishing_news()
            elif (publication_data['type']) == 'private ad':
                print('It`s private ad')
                text = publication_data['text']
                deadline_date = publication_data['deadline date']
                try:
                    expiration_date = datetime.strptime(deadline_date, '%Y/%m/%d')
                except:
                    print('Wrong date format!\nPlease repeat the input of ad with the right date format(yyyy/mm/dd)')

                if (expiration_date - current_date).days < 0:
                    print(
                        f'Wrong date was input - {deadline_date}\n'
                        f'Please repeat the input of ad with the right date (later than today)')
                else:
                    pass
                new_private_ad = PrivateAd(text, expiration_date)
                new_private_ad.publishing_ad()
            elif (publication_data['type']) == 'blog post':
                author = publication_data['author']
                title = publication_data['title']
                tag = publication_data['tag']
                text = publication_data['text']
                new_blogpost = BlogPost(text, title, author, tag)
                new_blogpost.publishing_post()
                print('It`s blog post')
            else:
                print('Unknown type')


class xmlReading:

    def validateXML(filepath):
        try:
            ET.parse(filepath)
        except ValueError as err:
            return False
        return True

    def read_xmlfile(filepath):
        with open(filepath, 'r') as xml_file:
            tree = ET.parse(filepath)
            root = tree.getroot()
            for child in root:
                print(child.tag, child.text)
            type = root.find("type").text

            if type.lower() == 'news':
                city = root.find("city").text
                text = root.find("text").text
                new_news = News(text, city)
                new_news.publishing_news()

            elif type.lower() == 'private ad':
                text = root.find("text").text
                expiration_date = root.find("expiration_date").text
                new_private_ad = PrivateAd(text, expiration_date)
                new_private_ad.publishing_ad()

            elif type.lower() == 'blog post':
                author = root.find("author").text
                title = root.find("title").text
                tag = root.find("tag").text
                text = root.find("text").text
                new_blogpost = BlogPost(text, title, author, tag)
                new_blogpost.publishing_post()

            else:
                print('Unknown type')


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


class FileCSV:

    def __init__(self):
        self.newsfeed = "normalized_newsfeed.txt"

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

        if os.path.exists("word_stat.csv"):
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
        upper = 0
        digits = 0

        for line in infile:
            wordslist = line.split()
            lines = lines + 1
            words = words + len(wordslist)
            characters += sum(len(word) for word in wordslist)

        all_freq = {}

        with open("normalized_newsfeed.txt") as file:
            text = file.read()
            text = text.lower()
            for i in text:
                if i.isupper():
                    upper += 1
                elif (i.isdigit()):
                    digits += 1

            text = ''.join([i for i in text if not i.isdigit()])
            all_punct = '''!()-[]{};:'="`\,<>./?@#$%^&*_~'''

            for elements in text:
                if elements in all_punct:
                    text = text.replace(elements, "")

            text = "".join(text.split())

            for i in text:
                if i in all_freq:
                    all_freq[i] += 1
                else:
                    all_freq[i] = 1

        if os.path.exists("letters_stat.csv"):
            os.remove("letters_stat.csv")
        else:
            print('File isn`t found')

        with open('letters_stat.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            for k, v in all_freq.items():
                writer.writerow([k, v])


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
                checkJSONfile = JSONReading
                isJsonFile = checkJSONfile.validateJSON(filepath)
                checkXMLfile = xmlReading
                isxmlfile = checkXMLfile.validateXML(filepath)
                if isJsonFile:
                    checkJSONfile.read_jsonfile(filepath)
                elif isxmlfile:
                    print('This is XML')
                    checkXMLfile.read_xmlfile(filepath)
                else:
                    upload_to_print = FileUpload(filepath)
                    upload_to_print.publishing_from_file()
                    upload_to_print.delete_file()

            elif os.path.isfile(fileinput):
                filepath = fileinput
                print('Another directory')
                checkJSONfile = JSONReading
                isJsonFile = checkJSONfile.validateJSON(filepath)
                checkXMLfile = xmlReading
                isxmlfile = checkXMLfile.validateXML(filepath)
                if isJsonFile:
                    checkJSONfile.read_jsonfile(filepath)
                elif isxmlfile:
                    print('This is XML')
                    checkXMLfile.read_xmlfile(filepath)
                else:
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
        csv = FileCSV()
        csv.count_words()
        csv.show_statistics()


if __name__ == "__main__":
    Main()