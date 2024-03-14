import requests


class NewsFinder:

    def __init__(self, symbol, dates):
        parameters = {
            "q": symbol,
            "from": dates[0],
            "to": dates[1],
            "sortBy": "popularity",
            "language": "en",
            "pageSize": 3,
            "apiKey": "LoremIpsum"
        }
        response = requests.get(url="https://newsapi.org/v2/everything", params=parameters)
        response.raise_for_status()
        self.news_data = response.json()

    def get_news(self):
        news_dict = []
        for news in self.news_data["articles"]:
            news_entry = {
                "title": news["title"],
                "description": news["description"],
                "link": news["url"]
            }
            news_dict.append(news_entry.copy())
        return news_dict
