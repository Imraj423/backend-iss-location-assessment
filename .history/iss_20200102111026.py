#!/usr/bin/env python3

__author__ = 'Imraj423'

import requests
import turtle


screen = turtle.Screen()
screen.bgpic("map.gif")
screen.screensize(400, 300)
my_turtle = turtle.Turtle()
my_turtle.shape("iss.gif")

r = requests.get('http://api.open-notify.org/astros.json')
print(r.text)

s = requests.get('http://api.open-notify.org/iss-now.json')
print(s.text)
