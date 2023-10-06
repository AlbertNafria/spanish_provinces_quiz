import turtle
import pandas

width = 1386
height = 823

screen = turtle.Screen()
screen.setup(width, height)
screen.title("Spanish Provinces Game")

image = "spanish_map.gif"
provinces_csv_file = "provinces.csv"

guessed_provinces = []

screen.addshape(image)
turtle.shape(image)

# Create dataset with pandas
data = pandas.read_csv(provinces_csv_file)
provinces_list = data.province.to_list()

print(len(provinces_list))

# Main loop
while len(guessed_provinces) < len(provinces_list):
    answer = screen.textinput(title=f"{len(guessed_provinces)}/{len(provinces_list)} provinces correct",
                              prompt="Tell me another province:").title()
    if answer == "Exit":
        missing_provinces = []
        for province in provinces_list:
            if province not in guessed_provinces:
                missing_provinces.append(province)
        # Save a list of missing provinces
        missing_provinces_data = pandas.DataFrame(missing_provinces)
        missing_provinces_data.to_csv("provinces_missing.csv")
        break

    if answer in provinces_list:
        guessed_provinces.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        province_data = data[data.province == answer]
        t.goto(int(province_data.x), int(province_data.y))
        t.write(answer)