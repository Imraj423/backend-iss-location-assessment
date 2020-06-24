import requests
import turtle


def iss_location():
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
    screen.delay(5)

    image = "iss.gif"
    screen.addshape(image)
    raf = turtle.Turtle()
    raf.shape(image)
    raf.setheading(45)
    raf.pendown()
    raf.goto(float(lat), float(lon))
    raf.penup()

    screen.exitonclick()
    return lat, lon


def astronauts():
    r = requests.get('http://api.open-notify.org/astros.json')
    data = r.json()
    r.raise_for_status()
    name = data["people"]["name"]
    craft = data["people"]["craft"]
    print("/nAstronaut: " + (name))
    print("Craft: " + (craft))
    return r


if __name__ == "__main__":
    iss_location(), astronauts()
