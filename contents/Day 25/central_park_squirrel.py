#Before you watch the solution, The aim of this challenge is to:
# - Divide Fur colors as columns 
# - Make another Fur column to count how many of each color are there:
import pandas 

data = pandas.read_csv(r"100-days-of-coding--Python-\contents\Day 25\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

counting = data["Primary Fur Color"].value_counts().to_dict()

keys_data = list(counting.keys())
values_data = list(counting.values())

new_dataframe = {
    'Fur Color' : keys_data,
    'Count' : values_data
}

as_dataframe = pandas.DataFrame(new_dataframe)
print(as_dataframe)