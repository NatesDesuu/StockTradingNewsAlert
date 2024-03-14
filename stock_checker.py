import requests


class StockChecker:

    def __init__(self, symbol, function):
        parameters = {
            "symbol": symbol,
            "function": function,
            "outputsize": "compact",
            "apikey": "LoremIpsum"
        }
        response = requests.get(url="https://www.alphavantage.co/query", params=parameters)
        response.raise_for_status()
        self.stock_data = response.json()
        try:
            self.last_refresh_date = self.stock_data["Meta Data"]["3. Last Refreshed"]
        except KeyError:
            print("Maximum number of requests today already reached.")
        else:
            self.stock_data_series = iter(self.stock_data["Time Series (Daily)"])

    def get_stock_dates(self):
        for series in self.stock_data_series:
            if series == self.last_refresh_date:
                second_day_date = next(self.stock_data_series, None)
                return self.last_refresh_date, second_day_date

        # # For testing purposes
        # return "2024-03-13", "2024-03-12"

    def get_stock_diff(self, dates):
        first_day_stock = float(self.stock_data["Time Series (Daily)"][dates[0]]["4. close"])
        second_day_stock = float(self.stock_data["Time Series (Daily)"][dates[1]]["4. close"])

        # # For testing purposes
        # first_day_stock, second_day_stock = 1000, 900

        percentage_diff = round(((first_day_stock - second_day_stock) / second_day_stock) * 100, 2)
        return percentage_diff
