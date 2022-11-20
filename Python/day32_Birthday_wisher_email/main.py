##################### Extra Hard Starting Project ######################
import datetime as dt
import pandas
import random
import smtplib

my_email="rdiazzz920@gmail.com"

now=dt.datetime.now()
year=now.year
month=now.month
day=now.day

data=pandas.read_csv("birthdays.csv")
data_list=data.to_dict(orient="records")

def send_mail():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email,password="kzynkywpsysxgizk")
        connection.sendmail(from_addr=my_email,to_addrs=f"{data['email']}",msg=f"Subject:Happy Birthday!\n\n{contents}")

for data in data_list:
    if data['day']==day and data['month']==month:
        with open(f"./letter_templates/letter_{random.randint(1,3)}.txt") as new_data:
            n=new_data.read()
            contents=n.replace("[NAME]",f"{data['name']}")
            send_mail()



