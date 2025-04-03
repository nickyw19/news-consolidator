from NewsApi import NewsApi
from NewsWebScraper import NewsWebScraper
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from flask import Flask, render_template
from dotenv import load_dotenv
import smtplib
import os

class NewsConstructor:
    articles = []
    articles_per_source = 5
    sources_from_api = [
        ("New York Times",     "https://api.nytimes.com/svc/topstories/v2/home.json"),
        ("The Guardian",       "https://content.guardianapis.com/search")
    ]
    sources_from_web = [
        ("Asia News Network", "https://asianews.network/tag/thailand/"),
        ("Channel News Asia",   "https://www.channelnewsasia.com/latest-news"),
        ("Forbes",              "https://www.forbes.com/news/"),
        ("TechCrunch",           "https://techcrunch.com/latest/")
    ]

    app = Flask(__name__)
    def __init__(self):
        load_dotenv()

    #Main method that calls all methods needed to extract and send the required data
    def get_and_send_articles(self):
        self.get_web_data()
        self.get_api_data()
        self.remove_duplicates()
        self.resize_list()
        self.send_email()

    #Extract news via Webscraping
    def get_web_data(self):
        news_scraper = NewsWebScraper(self.sources_from_web, self.articles_per_source)
        web_data = news_scraper.get_data()
        self.add_articles(web_data)

    #Extract news via API
    def get_api_data(self):
        news_api = NewsApi(self.sources_from_api, self.articles_per_source*(len(self.sources_from_web)+1))
        api_data = news_api.get_data()
        self.add_articles(api_data)

    #Add articles to the articles list
    def add_articles(self, data):
        if len(data) == 0:
            self.articles.append("No articles to add")
        else:
            for article in data:
                self.articles.append(article)

    #Remove duplicates (headlines that share 3 or more words)
    def remove_duplicates(self):
        index = self.articles_per_source
        formatted_list = []
        for num in range(self.articles_per_source):
            formatted_list.append(self.articles[num])

        while index < len(self.articles):
            add_article = True
            current_article = self.articles[index]
            for article in formatted_list:
                if article == "No articles to add":
                    continue
                article_to_compare = article['title'].lower().split(" ")
                article_to_add = current_article['title'].lower().split(" ")

                shared_words = list(set(article_to_compare) & set(article_to_add))
                filler_words = ["the","a","an",
                                "in","on","at","for","with","to","about",
                                "and","or", "but", "so", "of", "is", "are", "was", "has","have", "had"]

                shared_words = [word for word in shared_words if word not in filler_words]

                if len(shared_words) >= 3:
                    add_article = False
                    break
            if add_article:
                formatted_list.append(current_article)
            index += 1
        self.articles = formatted_list

    #Limit the # of articles per source to self.articles_per_source
    def resize_list(self):
        final_list = []
        current_source = ""
        switch_source = False
        for article in self.articles:
            if len(final_list) % 5 == 0 and len(final_list)!= 0:
                switch_source = True
            if switch_source and article["source"] == current_source:
                    continue
            else:
                current_source = article["source"]
                final_list.append(article)
                switch_source = False
        self.articles = final_list

    #Send extracted data via email
    def send_email(self):
        sender_email = os.getenv("SENDER_EMAIL")
        recipient_email = os.getenv("RECIPIENT_EMAIL")
        gmail_app_pw = os.getenv("GMAIL_APP_PW")

        try:
            with self.app.app_context():
                msg = MIMEMultipart()
                msg['From'] = sender_email
                msg['To'] = recipient_email
                msg['Subject'] = "The Brief"
                html_content = render_template('EmailContent.html', articles = self.articles )
                msg.attach(MIMEText(html_content, 'html'))
        except Exception as e:
            print(f"Error related to email creation. Error: {e}")
            return None

        try:
            connection = smtplib.SMTP("smtp.gmail.com",587,timeout=60)
            connection.starttls()
            connection.login(user = sender_email, password = gmail_app_pw)
            connection.sendmail(
                from_addr = sender_email,
                to_addrs = recipient_email,
                msg = msg.as_string()
            )
            print("Email sent successfully.")
            connection.close()
        except Exception as e:
            print(f"Failed to send email. Error: {e}")
            return None



