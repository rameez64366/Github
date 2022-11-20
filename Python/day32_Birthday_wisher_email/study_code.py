import random
import smtplib
import datetime as dt

my_email="rdiazzz920@gmail.com"
def send_mail():
    with smtplib.SMTP("smtp.gmail.com") as connection:  #smtp information
        connection.starttls()   # transport layer security(tls) is a way of securing our connection to server
                                # like someone intercept email it will show encrypted message
        connection.login(user=my_email,password="kzynkywpsysxgizk")
        connection.sendmail(from_addr=my_email,to_addrs="amyyysantiagooo@yahoo.com",msg=f"{quote}")

now=dt.datetime.now()
year=now.year
month=now.month
day=now.day
day_of_week=now.weekday()
if day_of_week==0:
    with open("quotes.txt") as data_file:
        data=data_file.readlines()
        quote=random.choice(data)
        send_mail()





