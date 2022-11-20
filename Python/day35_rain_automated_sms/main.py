import requests
from twilio.rest import Client
import os
API_KEY="2597cb59689f5af76124a275bd37d967"
API_ENDPOINT="https://api.openweathermap.org/data/2.5/forecast"
MY_LAT=53.508598
MY_LONG=49.419834

accound_sid=os.environ.get("ACCOUNT_SID")
auth_token=os.environ.get("AUTH_TOKEN")



parameters={
    "lat":MY_LAT,
    "lon":MY_LONG,
    "appid":API_KEY,
}


response=requests.get(url=API_ENDPOINT,params=parameters)
response.raise_for_status()

data=response.json()
print(data)
will_rain=False
weather_data_ID=[]
for i in range(0,12):
    weather_data_ID.append(data['list'][i]['weather'][0]['id'])
print(weather_data_ID)

for val in weather_data_ID:
    if val<700:
        will_rain=True

if will_rain:
    print("bring an umbrella")
    # client=Client(accound_sid,auth_token)
    #
    # message = client.messages \
    #     .create(
    #     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
    #     from_='+15017122661',
    #     to='+15558675310'
    # )







