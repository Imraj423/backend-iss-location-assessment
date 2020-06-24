import requests
import turtle

screen = turtle.Screen()
image = "iss.gif"
screen.addshape(image)
raf = turtle.Turtle()
raf.shape(image)
screen.bgpic("map.gif")
screen.screensize(400, 300)
screen.setup(width=200, height=200, startx=0, starty=0)

r = requests.get('http://api.open-notify.org/astros.json')
print(r.text)

s = requests.get('http://api.open-notify.org/iss-now.json')
print(s.text)
