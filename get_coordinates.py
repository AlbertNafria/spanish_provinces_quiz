import turtle

width = 1386
height = 823

screen = turtle.Screen()
screen.setup(width, height)
screen.title("Spanish Provinces Game")

image = "spanish_map.gif"

screen.addshape(image)
turtle.shape(image)


def get_mouse_click_coor(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()