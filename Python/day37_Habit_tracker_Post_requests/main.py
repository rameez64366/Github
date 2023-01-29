import requests
import datetime as dt

today=dt.datetime.now()
# year=now.year
# month=now.month
# day=now.day
# date=str(year)+str(month)+str(day)

today=today.strftime("%Y%m%d")
print(today)

###################Pixela##########
Pixela_end_point="https://pixe.la/v1/users"
TOKEN="fefefefseeww"
USER_NAME="rameez64366"
GRAPH_ID="graph1"
user_params={
    "token":TOKEN,
    "username":USER_NAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}
# response=requests.post(url=Pixela_end_point,json=user_params)
# print(response.text)

#############graph##########
graph_endpoint=f"{Pixela_end_point}/{USER_NAME}/graphs"
graph_params={
    "id":GRAPH_ID,
    "name":"Cycling graph",
    "unit":"Km",
    "type":"float",
    "color":"ajisai"
}

headers={
    "x-USER-TOKEN":TOKEN
}

# response=requests.post(url=graph_endpoint,json=graph_params,headers=headers)
# print(response.text)

# #######################post################
post_api_end_point=f"{Pixela_end_point}/{USER_NAME}/graphs/{GRAPH_ID}"
post_parameters={
    "date":today,
    "quantity":"9.74"
}

# response=requests.post(url=post_api_end_point,json=post_parameters,headers=headers)
# print(response.text)

#####################Put Pixel#######################

post_put_endpoint=f"{Pixela_end_point}/{USER_NAME}/graphs/{GRAPH_ID}/{today}"

post_put_parameters={
    "quantity":"8"
}

# response=requests.put(url=post_put_endpoint,json=post_put_parameters,headers=headers)
# print(response.text)

####################### Delete Pixel ###################

response=requests.delete(url=post_put_endpoint,headers=headers)
print(response.text)
