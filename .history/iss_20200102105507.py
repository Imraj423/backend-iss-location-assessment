#!/usr/bin/env python3

__author__ = 'Imraj423'

import requests
import turtle


wb = my_turtle.Screen()
wb.bgcolor("light green")
my_turtle = turtle.Turtle()






r = requests.get('http://api.open-notify.org/astros.json')
print(r.text)

s = requests.get('http://api.open-notify.org/iss-now.json')
print(s.text)


# if __name__ == '__main__':
#     main()
