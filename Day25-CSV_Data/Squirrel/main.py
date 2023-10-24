import pandas

data = pandas.read_csv("squirrel.csv")
fur_color_data = data['Primary Fur Color'].value_counts().to_list()

# squirrel_dict = {
#     "Fur Color": ["Gray", "Cinnamon", "Black"],
#     "Count": fur_color_data
# }

# squirrel = pandas.DataFrame(squirrel_dict)
# squirrel.to_csv("Squirrel_count.csv")

