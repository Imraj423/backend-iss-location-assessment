import requests
import turtle
import time


def iss_location():
    while True:
        try:
            s = requests.get('http://api.open-notify.org/iss-now.json')
            data = s.json()
            s.raise_for_status
            lat = data["iss_position"]["latitude"]
            lon = data["iss_position"]["longitude"]

            print("\nLatitude: " + str(lat))
            print("Longitude: " + str(lon))
            screen = turtle.Screen()
            screen.bgpic("map.gif")
            screen.screensize(800, 600)
            screen.setup(720, 360)
            screen.setworldcoordinates(-180, -90, 180, 90)
            screen.delay(1)

            image = "iss.gif"
            screen.addshape(image)
            raf = turtle.Turtle()
            raf.shape(image)
            raf.setheading(45)
            raf.speed(7)
            raf.goto(float(lat), float(lon))
            time.sleep(10)
            screen.exitonclick()
            return lat, lon



 if __name__ == "__main__":
    iss_location()
