import turtle
import random

t = turtle.Turtle()
t.screen.title("Bambi with Freckles :)")
t.screen.bgcolor("red")

def head(x, y, size, tilt, color):
    t.color(color)
    t.begin_fill()
    
    t.up()
    t.goto(x,y)
    t.down()
    t.seth(270 + tilt)
    t.circle(size, 180)
    t.circle(2 * size, 45)
    t.circle(0.58 * size, 90)
    t.circle(2 * size, 45)
    
    t.end_fill()

def eyes(x, y, r, color):
    t.color(color)
    t.begin_fill()
    
    t.up()
    t.goto(x,y)
    t.down()
    t.circle(r)
    
    t.end_fill()

def ears(x, y, br, sr, tilt, color):
    t.color(color)
    t.begin_fill()
    
    t.up()
    t.goto(x,y)
    t.down()
    t.seth(-45+tilt)
    t.circle(br,90)
    t.circle(sr,90)
    t.circle(br,90)
    t.circle(sr,90)

    t.end_fill()

def stars(color):
    t.color(color)
    x = random.randrange(-200, -100)
    y = random.randrange(-200, -100)
    
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.circle(10)
    t.end_fill()


head(0, 0, 150, -180, "peru")
eyes(-20, 0, 30, "skyblue")
eyes(-200, 0, 30, "skyblue")
ears(-30, 120, 120, 35, 90, "peachpuff")
ears(-225, 120, 120, 35, 90, "peachpuff")

for i in range(10):
    stars("sandybrown")
