from stock_checker import StockChecker
from news_finder import NewsFinder
from sms_sender import SMSSender

SYMBOL = "LoremIpsum"
COMPANY_NAME = "LoremIpsum"
FUNCTION = "TIME_SERIES_DAILY"

stock = StockChecker(SYMBOL, FUNCTION)
stock_dates = stock.get_stock_dates()
stock_percent = stock.get_stock_diff(stock_dates)

# # For testing purposes
# print(f"{stock_dates}\n{stock_percent}")

if abs(stock_percent) >= 5:
    news = NewsFinder(COMPANY_NAME, stock_dates).get_news()
    sms = SMSSender(SYMBOL, stock_percent, news)
    sms.send_sms()
else:
    print("No drastic movement in the symbol's stock price observed.")
