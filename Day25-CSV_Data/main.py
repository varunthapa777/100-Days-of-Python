import pandas

data = pandas.read_csv("C:/Users/arun/varun/git/python/Day25-CSV_Data/weather_data.csv")

# avg_temp = data['temp'].mean()
# max_temp = data['temp'].max()
#
# print(avg_temp)
# print(max_temp)
#
# # get data in column
# print(data.day)
# print(data.['day']
#
# get data in row
print(data[data.day == "Monday"])
print(data[data.temp == data['temp'].max()])
# day_temp = data[data.day == "Monday"].temp
# day_temp_F = day_temp * 9/5 + 32
# print(day_temp_F)

# create data frame from scratch
# data_dict = {
#     "students": ["Varun", "Arun", "Sidhu"],
#     "score": [90, 80, 99]
# }
# student = pandas.DataFrame(data=data_dict)
# student.to_csv("students.csv")

