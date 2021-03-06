import requests
import turtle
import time
import json
from datetime import datetime

raf = turtle.Turtle()


def get_astronauts():
    response = requests.get('http://api.open-notify.org/astros.json')
    response.raise_for_status()
    astro_dict = {}
    astronauts = response.json()['people']
    for name_obj in astronauts:
        astro_dict[name_obj['name']] = name_obj['craft']
    return astro_dict


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
        response.raise_for_status

        loc = result["iss_position"]
        lat = loc["latitude"]
        lon = loc["longitude"]

        raf.speed(7)
        
        print("\nLatitude: " + str(lat))
        print("Longitude: " + str(lon))
        
        raf.goto(lon, lat)
        time.sleep(5)


def over_ind():
    parameters = {'lat': 39.7684, 'lon': -86.1581}
    response = requests.get(
        "http://api.open-notify.org/iss-pass.json", params=parameters)
    pass_times = response.json()['response']
    risetimes = []
    for d in pass_times:
        time = d['risetime']
        risetimes.append(time)
    times = []
    for rt in risetimes:
        time = datetime.fromtimestamp(rt)
        times.append(time)
    print("The ISS will be over Indianapolis at the following times:{}".format(time))
    astro_dict = get_astronauts()
    print(f"There are currently {len(astro_dict)} astronauts in space!")
    for name in astro_dict:
        print(f'    {name} is on the {astro_dict[name]}')


if __name__ == "__main__":
    get_astronauts(), over_ind(), draw_map(), iss_location()
