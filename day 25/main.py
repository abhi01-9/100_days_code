# with open("weather_data.csv") as file:
#     data = file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1]!="temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas as pd

data = pd.read_csv("weather_data.csv")
# print(data["temp"])
# print(type(data))
data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

print(f"average temperature {data["temp"].mean()}")
print(f"max temperature {data["temp"].max()}")

# get data in column
print(data["condition"])
print(data.condition)

# Get data in Row

print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

print(data[data.temp == data.temp.max()].temp)

# Creating a DataFrame from scratch

data_dict = {
    "student": ["abhi", "bhaskar", "rahul"],
    "score": [76, 56, 65]
}

data = pd.DataFrame(data_dict)
print(data)
#Creating Csv data
# data.to_csv("new_data.csv")


