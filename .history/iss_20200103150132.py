import requests
import turtle
import time

raf = turtle.Turtle()


def draw_map():
    screen = turtle.Screen()
    screen.bgpic("map.gif")
    screen.screensize(800, 600)
    screen.setup(720, 360)
    screen.setworldcoordinates(-180, -90, 180, 90)
    image = "iss.gif"
    screen.addshape(image)
    
    raf.shape(image)
    raf.setheading(45)
    raf.penup()
    screen.exitonclick()


def iss_location():
    while True:
        response = requests.get('http://api.open-notify.org/iss-now.json')
        result = json.loads(response.read())
        s.raise_for_status

        lat = data["iss_position"]["latitude"]
        lon = data["iss_position"]["longitude"]

        raf.speed(7)
        
        print("\nLatitude: " + str(lat))
        print("Longitude: " + str(lon))
        
        raf.goto(lat, lon)
        time.sleep(5)


if __name__ == "__main__":
    draw_map(), iss_location()
