import requests
from datetime import date, timedelta
from twilio.rest import Client
import smtplib

STOCK = "AMZN"
COMPANY_NAME = "Amazon Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

api_key_stock = ""
api_key_news = ""

theme = "amazon"

from_tel = "+"
to_tel = "+"
account_sid = ""
auth_token = ""

from_date = str(date.today() - timedelta(days=2))
print(from_date)

to_date = str(date.today() - timedelta(days=1))
print(to_date)

params_stock = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": api_key_stock
}

params_news = {
    "q": theme,
    "from": from_date,
    "to": to_date,
    "sortBy": "popularity",
    "apiKey": api_key_news
}

response_stock = requests.get(STOCK_ENDPOINT, params=params_stock)
response_stock.raise_for_status()

stock_price1 = float(response_stock.json()["Time Series (Daily)"][from_date]["4. close"])
stock_price2 = float(response_stock.json()["Time Series (Daily)"][to_date]["4. close"])

price_difference = stock_price2 - stock_price1
price_difference_percent = round(price_difference / stock_price2 * 100)

up_down = None
if price_difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"


if abs(price_difference) > 1:  # CHANGE SIGN TO >
    news_response = requests.get(NEWS_ENDPOINT, params=params_news)
    news_response.raise_for_status()
    articles = news_response.json()["articles"]
    three_articles = articles[:3]
    formatted_articles = [f"{STOCK}: {up_down}{price_difference_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

    client = Client(account_sid, auth_token)
    for article in formatted_articles:
        message = client.messages \
            .create(
            body=article,
            from_=from_tel,
            to=to_tel
        )

    # connection = smtplib.SMTP("smtp.gmail.com", 587)
    # connection.starttls()
    # connection.login(my_email, pass)
    # connection.sendmail(from_addr=my_email,
    #                     to_addrs=birthday_person["email"],
    #                     msg=f"Subject:Happy Birthday\n\n{contents}")

## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
# HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
# HINT 2: Work out the value of 5% of yerstday's closing stock price.

## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
# HINT 1: Think about using the Python Slice Operator


## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
# HINT 1: Consider using a List Comprehension.


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
