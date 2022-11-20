import os
import smtplib
import requests
import datetime as dt
import re




##########################date##########
now=dt.datetime.now()
year=now.year
month=now.month
today=now.day

####################company#################
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
def company():
    alpha_vantage_endpoint="https://www.alphavantage.co/query"
    alpha_vantage_support_API_key=os.environ.get("ALPHA_VANTAGE_API_KEY")
    alpha_vantage_parameters={
        "function":"TIME_SERIES_DAILY_ADJUSTED",
        "symbol":STOCK,
        "apikey":alpha_vantage_support_API_key
    }

    response=requests.get(url=alpha_vantage_endpoint,params=alpha_vantage_parameters)
    response.raise_for_status()
    alpha_data=response.json()
    return alpha_data
####################news###################
def news():
    news_API_key=os.environ.get("NEWS_API_KEY")
    news_API_endkey="https://newsapi.org/v2/everything"
    news_parameter={
        "q":COMPANY_NAME,
        "apiKey":news_API_key
    }
    response=requests.get(url=news_API_endkey,params=news_parameter)
    response.raise_for_status()

    data=response.json()['articles']
    three_articles=data[:3]
    return three_articles

##############################E-mail#######################

MY_Email="rdiazzz920@gmail.com"
MY_Password="kzynkywpsysxgizk"
To_mail_address="amyyysantiagooo@yahoo.com"



alpha_data=company()
three_articles=news()

formatted_article=[f"Subject:{article['title']} {article['description']}" for article in three_articles]
stock_price_closed=[]
for i in range(1,3):
    stock_price_closed.append(alpha_data["Time Series (Daily)"][f"{year}-{month}-{today-i}"]["4. close"])


percentage=round((abs(float(stock_price_closed[0])-float(stock_price_closed[1]))/float(stock_price_closed[0]))*100,2)

updated_formatted_article=[re.sub(r'https?://\S+','',article)  for article in formatted_article]
new_format=[article.replace('<a href=" target="_blank">(TSLA.O)</a>','') for article in updated_formatted_article]

if percentage>1:
    for k in new_format:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_Email, password=MY_Password)
            connection.sendmail(from_addr=MY_Email, to_addrs=To_mail_address, msg=f"{k}")




## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


