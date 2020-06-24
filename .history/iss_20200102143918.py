import requests
import turtle


def main():
    payload = {'latitude': key1, 'longitude': key2}
    s = requests.get('http://api.open-notify.org/iss-now.json',
                     data=payload)
    s.json
    s.raise_for_status

    lat = payload["latitude"]
    lon = payload["longitude"]

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
    raf.goto(lat, lon)
    raf.penup()

    screen.exitonclick()




def astronauts():
    r = requests.get('http://api.open-notify.org/astros.json')
    r.json
    r.raise_for_status()
    print(r.text)
    return r


if __name__ == "__main__":
    main()
