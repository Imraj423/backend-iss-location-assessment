import requests
import turtle


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


def main():
    while True:
        
        s = requests.get('http://api.open-notify.org/iss-now.json')
        s.json
        s.raise_for_status
        print(s.text)
    
    location = s["iss_position"]
    lat = location["latitude"]
    lon = location["longitude"]

    print("\nLatitude: " + str(lat))
    print("Longitude: " + str(lon))

    raf.goto(lon, lat)
    time.sleep(5)

def astronauts():
    r = requests.get('http://api.open-notify.org/astros.json')
    r.json
    r.raise_for_status()
    print(r.text)
    return r


if __name__ == "__main__":
    main()
