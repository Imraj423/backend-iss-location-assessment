import requests
import turtle

screen = turtle.Screen()
image = "iss.gif"
screen.addshape(image)
raf = turtle.Turtle()
raf.shape(image)
raf.setheading(90)
raf.penup()

screen.bgpic("map.gif")
screen.screensize(4000, 3000)
screen.setup(width=800, height=600, startx=0, starty=0)
screen.exitonclick()
while True:
    s = requests.get('http://api.open-notify.org/iss-now.json')
    s.raise_for_status
    result = json.loads(s.read())
    print(s.text)

  #Let's extract the required information
    location = result["iss_position"]
    lat = location["latitude"]
    lon = location["longitude"]

    #Output informationon screen
    print("\nLatitude: " + str(lat))
    print("Longitude: " + str(lon))

    #Plot the ISS on the map
    raf.goto(lon, lat)
    #refresh position every 5 seconds
    time.sleep(5)

r = requests.get('http://api.open-notify.org/astros.json')
r.raise_for_status()
print(r.text)



