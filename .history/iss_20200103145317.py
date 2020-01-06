import requests
import turtle
import time


def draw_map():
    screen = turtle.Screen()
    screen.bgpic("map.gif")
    screen.screensize(800, 600)
    screen.setup(720, 360)
    screen.setworldcoordinates(-180, -90, 180, 90)
    image = "iss.gif"
    screen.addshape(image)
    raf = turtle.Turtle()
    raf.shape(image)
    raf.setheading(45)
    raf.penup()
    screen.exitonclick()


def iss_location():
    while True:

        s = requests.get('http://api.open-notify.org/iss-now.json')
        data = s.json()
        s.raise_for_status
        lat = data["iss_position"]["latitude"]
        lon = data["iss_position"]["longitude"]

        print("\nLatitude: " + str(lat))
        print("Longitude: " + str(lon))
        return lat, lon


if __name__ == "__main__":
    iss_location()
