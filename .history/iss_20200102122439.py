import requests
import turtle


screen = turtle.Screen()
image = "iss.gif"
screen.addshape(image)
raf = turtle.Turtle()
raf.shape(image)
raf.setheading(45)
raf.penup()

screen.bgpic("map.gif")
screen.screensize(800, 600)
screen.setup(720, 360)
screen.setworldcoordinates(-180, -90, 180, 90)
screen.exitonclick()


def location():
    s = requests.get('http://api.open-notify.org/iss-now.json')
    s.raise_for_status
    print(s.status_code)


def astronauts():
    r = requests.get('http://api.open-notify.org/astros.json')
    r.raise_for_status()
    print(r.text)

