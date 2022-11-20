import requests
import smtplib
import datetime as dt
MY_LAT=-42.0329
MY_LONG=-73.3286
MY_COORDINATE=(MY_LAT,MY_LONG)
my_email="rdiazzz920@gmail.com"
Password="kzynkywpsysxgizk"

to_mail="amyyysantiagooo@yahoo.com"

def iss_overhead():
    response=requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data=response.json()

    iss_latitude=float(data["iss_position"]["latitude"])
    iss_longitude=float(data["iss_position"]["longitude"])
    print((iss_latitude,iss_longitude))

    def your_positon():
        if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5<= iss_longitude <= MY_LONG+5:
            return True







def is_night():
    parameters={
        "lat":MY_LAT,
        "lng":MY_LONG,
        "formatted":0
    }

    response=requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
    response.raise_for_status()


    data=response.json()

    sunrise=data['results']['sunrise']
    sunset=data['results']['sunset']

    sunrise_24h_format=int(sunrise.split("T")[1].split(":")[0])
    sunset_24h_format=int(sunset.split("T")[1].split(":")[0])

    now=dt.datetime.now()
    current_hour=now.hour

    if current_hour>=sunset_24h_format and current_hour<=sunrise_24h_format:
        return True

if iss_overhead() and is_night():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email,password=Password)
        connection.sendmail(from_addr=my_email,to_addrs=to_mail,msg="Subject:Look up\n\nThe ISS is above you")