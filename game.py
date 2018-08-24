# coding: utf-8

import turtle
import random
import math

phi = 360/7
r = 70


def gotoxy(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


def color_circle(r, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()


def revolver(base_x, base_y):
    # Основная окружность
    gotoxy(base_x, base_y)
    turtle.circle(110)
    # Мушка
    gotoxy(base_x, base_y + 220)
    color_circle(10, "red")
    # Барабан
    for i in range(0, 7):
        phi_rad = phi * i * math.pi / 180.0
        gotoxy(base_x + math.sin(phi_rad) * r, base_y + math.cos(phi_rad) * r + 78)
        color_circle(30, "white")


def rev_animation(base_x, base_y, start):
    for i in range(start, random.randrange(7, 100)):
        phi_rad = phi * i * math.pi / 180.0
        gotoxy(base_x + math.sin(phi_rad) * r, base_y + math.cos(phi_rad) * r + 78)
        color_circle(30, "black")
        color_circle(30, "white")

    gotoxy(base_x + math.sin(phi_rad) * r, base_y + math.cos(phi_rad) * r + 78)
    color_circle(30, "brown")
    return i % 7


turtle.speed(0)
revolver(100, 50)

answer = " "
start = 0
while answer != "N":
    answer = turtle.textinput("Хотите поиграть?", "Y/N")
    if answer == "Y":
        rev_animation(100, 50, start)

        if start == 0:
            gotoxy(-150, 250)
            turtle.write("Вы проиграли!", font=("Arial", 18, "normal"))
    else:
        pass
