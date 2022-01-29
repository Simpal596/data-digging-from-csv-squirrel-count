import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
data_dict = {}
grey = 0
red = 0
black = 0
for item in data["Primary Fur Color"]:
    if item == "Gray":
        grey += 1
    elif item == "Cinnamon":
        red += 1
    elif item == "Black":
        black += 1

data_dict["fur_color"] = ["grey", "red", "black"]
data_dict["count"] = [grey, red, black]
sorted_data = pandas.DataFrame(data_dict)
sorted_data.to_csv('squirrel_count.csv')
