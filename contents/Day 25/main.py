#option 1
#instead open with csv library so you can get clean data
# with open(r"100-days-of-coding--Python-\contents\Day 25\weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

#option 2- good but not great especially for big databases
# import csv

# with open(r"100-days-of-coding--Python-\contents\Day 25\weather_data.csv") as data_file:
#     #will make data as an object not as a list as above
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != 'temp':
#             temperature.append(int(row[1]))
            
#     print(temperature)

#option 3- use pandas
import pandas

data = pandas.read_csv(r"100-days-of-coding--Python-\contents\Day 25\weather_data.csv")
print(data["temp"])

temp_list = data["temp"].to_list()
#to find the average 
#ave = sum(temp_list)/(len(temp_list))
#print(ave)

#to find the average with pandas
print(data["temp"].mean())

#to print the max 
print(data["temp"].max())

#How to get hold of columns in dataframe with pandas (2-ways)
data["condition"]
data.condition

#how to get hold of the rows in dataframe with pandas (2-ways)
data[data.day == "Monday"]
print(data[data["day"] == "Monday"])

#to get the row where the max was 
print(data[data["temp"] == data["temp"].max()])

#to get hold of only an item under specific column we do:
monday = data[data.day == "Monday"]
print(monday.condition)

#CHALLENGE 
#Convert Monday's temp to fahrenheit 
monday_temp = monday.temp
temp_to_fh = (monday_temp * 9/5) + 32 
print(temp_to_fh)

#how to create a dataframe from scratch
class_info = {
    "students" : ["Anna", "Antonela"],
    "grades" :[90,96]
}
#to convert it to a dataframe
new_dataframe = pandas.DataFrame(class_info)
print(new_dataframe)

#if you want to save it under day 25 
new_dataframe.to_csv(r"100-days-of-coding--Python-\contents\Day 25\new_dataframe.csv")