import urllib.request
import turtle
import time
import json

raf = turtle.Turtle()


def astronauts():
    url = "http://api.open-notify.org/astros.json"
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())
    print("There are currently " + str(result["number"]) + " astronauts in space:")
    print("")
    people = result["people"]

    for p in people:
        print(p["name"] + " on board of " + p["craft"])


def draw_map():
    screen = turtle.Screen()
    screen.bgpic("map.gif")
    screen.setup(720, 360)
    screen.setworldcoordinates(-180, -90, 180, 90)
    screen.addshape("iss.gif")
    
    raf.shape("iss.gif")
    raf.setheading(45)
    raf.penup()
    screen.exitonclick()


def iss_location():
    while True:
        url = "http://api.open-notify.org/iss-now.json"
        response = urllib.request.urlopen(url)
        result = json.loads(response.read())

        loc = result["iss_position"]
        lat = loc["latitude"]
        lon = loc["longitude"]

        raf.speed(7)
        
        print("\nLatitude: " + str(lat))
        print("Longitude: " + str(lon))
        
        raf.goto(lon, lat)
        time.sleep(5)


if __name__ == "__main__":
    astronauts(), draw_map(), iss_location()
