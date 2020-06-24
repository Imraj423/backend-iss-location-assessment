import requests
import turtle

screen = turtle.Screen()
image = "iss.gif"
screen.addshape(image)
raf = turtle.Turtle()
raf.shape(image)
raf.setheading(90)

screen.bgpic("map.gif")
screen.screensize(4000, 3000)
screen.setup(width=200, height=200, startx=0, starty=0)
screen.exitonclick()


r = requests.get('http://api.open-notify.org/astros.json')
r.raise_for_status()
print(r.text)


s = requests.get('http://api.open-notify.org/iss-now.json')
r.raise_for_status
print(s.text)
