import requests
import os
from dotenv import load_dotenv

class NewsApi:

    def __init__(self, sources, article_count):
        self.sources = sources
        self.article_count = article_count
        load_dotenv()

    #Retrieve a specified amount of articles from each API News Source
    def get_data(self):
        article_data = []
        for source in self.sources:
            if source[0] == "New York Times":
                data = self.get_nyt_data(source[1],self.article_count)
            elif source[0] == "The Guardian":
                data = self.get_guardian_data(source[1],self.article_count)
            else:
                data = []
            article_data.extend(data)
            self.article_count += 5
        return article_data

    #Make an HTTP Get request to the News Source's API and return the data extracted
    def request_data(self,source_link,parameters):
        response = requests.get(url=source_link, params=parameters)
        response.raise_for_status()
        return response

    #Extract New York Time's data via API, format it, and return it
    def get_nyt_data(self, api, count):
        articles = []
        params = {
            "api-key": os.getenv("NYT_API_KEY"),
        }
        response = self.request_data(api,params)

        data = response.json()["results"][:count]
        for article in data:
            temp_data = {
                "title": article['title'].split("|")[0].strip(),
                "url": article['url'],
                "source": "New York Times",
            }
            articles.append(temp_data)

        return articles

    # Extract Guardian's data via API, format it, and return it
    def get_guardian_data(self, api, count):
        articles = []
        params = {
            "api-key": os.getenv("GUARDIAN_API_KEY"),
            "page-size": 50,
        }
        response = self.request_data(api, params)
        data = response.json()["response"]["results"][:count]
        for article in data:
            temp_data = {
                "title": article["webTitle"].strip(),
                "url": article['webUrl'],
                "source": "The Guardian",
            }
            articles.append(temp_data)

        return articles
