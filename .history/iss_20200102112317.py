import requests
import turtle

screen = turtle.Screen()
image = "iss.gif"
screen.addshape(image)
turtle.shape(image)
screen.bgpic("map.gif")
screen.screensize(400, 300)



r = requests.get('http://api.open-notify.org/astros.json')
print(r.text)

s = requests.get('http://api.open-notify.org/iss-now.json')
print(s.text)
