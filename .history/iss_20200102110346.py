#!/usr/bin/env python3

__author__ = 'Imraj423'

import requests
import turtle

ship = "iss.gif"
def main():
    screen = turtle.Screen()
    screen.bgpic("map.gif")
    my_turtle = turtle.Turtle()
    my_turtle.shape("ship")






    r = requests.get('http://api.open-notify.org/astros.json')
    print(r.text)

    s = requests.get('http://api.open-notify.org/iss-now.json')
    print(s.text)


if __name__ == '__main__':
    main()
