import pandas

data_list=pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
#all_colors=data_list['Primary Fur Color']
count_grey=len(data_list[data_list["Primary Fur Color"]=="Gray"])
count_cinnamon=len(data_list[data_list["Primary Fur Color"]=="Cinnamon"])
count_black=len(data_list[data_list["Primary Fur Color"]=="Black"])
new_data={
    "Primary Fur Color":["grey","red","black"],
    "Count":[count_grey,count_cinnamon,count_black]
}
new_data_frame=pandas.DataFrame(new_data)
new_data_frame.to_csv("color_data_set.csv")




# import csv
# with open("weather_data.csv") as datas:
#    data=csv.reader(datas)
#    temperatures=[]
#    for row in data:
#        if row[1]!="temp":
#            temperatures.append(int(row[1]))
# print(temperatures)


#data=pandas.read_csv("weather_data.csv")

#print(data[data['temp']==data['temp'].max()])
# monday=data[data.day=="Monday"]
# degrees=monday.temp
# farenheit=(degrees*9/5)+32
# print(farenheit)


# data_dict={
#     "students":["amy","jake","angela"],
#     "scores":[90,70,80]
# }
# data=pandas.DataFrame(data_dict)
# print(data)











































