import requests
import turtle
import time
import json


screen = turtle.Screen()
image = "iss.gif"
screen.addshape(image)
raf = turtle.Turtle()
raf.shape(image)
raf.setheading(90)
raf.penup()

screen.bgpic("map.gif")
screen.screensize(800, 600)
screen.setup(width=800, height=600, startx=0, starty=0)
screen.setworldcoordinates(-180, -90, 180, 90)
screen.exitonclick()
while True:
    s = requests.get('http://api.open-notify.org/iss-now.json')
    s.raise_for_status
    result = json.loads(s.read())
    print(s.text)

    location = result["iss_position"]
    lat = location["latitude"]
    lon = location["longitude"]

    print("\nLatitude: " + str(lat))
    print("Longitude: " + str(lon))

    raf.goto(lon, lat)
    time.sleep(5)

r = requests.get('http://api.open-notify.org/astros.json')
r.raise_for_status()
result = json.loads(r.read())
print("There are currently " + str(result["number"]) + " astronauts in space:")
print("")

people = result["people"]

for p in people:
  print(p["name"] + " on board of " + p["craft"])
