from math import pi
type_of_the_figure = input()
if type_of_the_figure == "square":
    side = float(input())
    area = side * side
    print(f"{area:.3f}")

elif type_of_the_figure == "rectangle": #else if
    first_side = float(input())
    second_side = float(input())
    area = first_side * second_side
    print(f"{area:.3f}")
elif type_of_the_figure == "circle":
    radius = float(input())
    area = pi * (radius ** 2)
    print(f"{area:.3f}")
elif type_of_the_figure == "triangle": #else
    lenght = float(input())
    height = float(input())
    area = lenght * height / 2
    print(f"{area:.3f}")