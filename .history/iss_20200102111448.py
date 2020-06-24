import requests
import turtle

image = "iss.gif"
screen = turtle.Screen()
screen.bgpic("map.gif")
screen.screensize(400, 300)
screen.addshape(image)
turtle.Shape(image)


r = requests.get('http://api.open-notify.org/astros.json')
print(r.text)

s = requests.get('http://api.open-notify.org/iss-now.json')
print(s.text)
