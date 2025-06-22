from bs4 import BeautifulSoup
import requests

class NewsWebScraper:

    def __init__(self, url_list, article_count):
        self.url_list = url_list
        self.article_count = article_count
        self.article_data = []

    # Retrieve a specified amount of articles from each News Source via WebScraping
    def get_data(self):
        for source in self.url_list:
            self.get_html(source[0],source[1],self.article_count)
            self.article_count += 5
        return self.article_data

    # Make an HTTP Get request to the News Source's website and extract data using BeautifulSoup
    def get_html(self, news_source, url, num):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        json_data = ""
        if news_source == "Channel News Asia":
            json_data = soup.find_all(class_ = "h6__link list-object__heading-link")[:num]

        elif news_source == "Forbes":
            json_data = soup.find_all(class_="_1-FLFW4R")[:num]

        elif news_source == "Asia News Network":
            json_data = soup.find_all(class_="entry-title")[:num]

        elif news_source == "TechCrunch":
            json_data = soup.find_all(class_="loop-card__title-link")[:num]


        for article in json_data:
            headline = article.getText().strip()
            if news_source == "Asia News Network":
                url = str(article).split('"')[3]
            elif news_source == "Channel News Asia":
                url = "https://www.channelnewsasia.com"+str(article.get("href"))
            else:
                url = article.get("href")
            data = {
                "title": headline,
                "url": url,
                "source": news_source,
                }
            self.article_data.append(data)

