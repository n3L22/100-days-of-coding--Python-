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
