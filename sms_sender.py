from twilio.rest import Client


class SMSSender:

    def __init__(self, symbol, stock_percent, news):
        self.symbol = symbol
        self.percent = abs(stock_percent)
        self.news = news
        self.arrow = "🔺" if stock_percent > 0 else "🔻"

    def send_sms(self):
        account_sid = "LoremIpsum"
        auth_token = "LoremIpsum"
        client = Client(account_sid, auth_token)

        for news in self.news:
            line_1 = f"{self.symbol}: {self.arrow}{self.percent}%"
            line_2 = f"Headline: {news["title"]}"
            line_3 = f"Brief: {news["description"]}"
            line_4 = f"Link: {news["link"]}"

            # # For testing purposes
            # print(f"{line_1}\n{line_2}\n{line_3}\n{line_4}")

            message = client.messages \
                .create(
                body=f"{line_1}\n{line_2}\n{line_3}\n{line_4}",
                from_="LoremIpsum",
                to="+LoremIpsum"
            )
            print(message.status)
