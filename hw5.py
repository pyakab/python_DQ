from datetime import date, datetime

#Create a tool, which will do user generated news feed:
#1.User select what data type he wants to add
#2.Provide record type required data
#3.Record is published on text file in special format

#You need to implement:

#1.News – text and city as input. Date is calculated during publishing.

#2.Privat ad – text and expiration date as input. Day left is calculated during publishing.

#3.Your unique one with unique publish rules.

#Each new record should be added to the end of file. Commit file in git for review.

current_date = datetime.today()

class Publication():
    def __init__(self, text):
        self.text = text
        #self.city = city

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




class main():
    y = 0
    while y==0 :
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

        print('Do you want to add another publication? (Options: y/n)')
        user_answer = input()
        if user_answer == 'y':
            y = 0
        else:
            y = 1



main()
