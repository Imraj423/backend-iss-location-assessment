#!/usr/bin/env python3

__author__ = 'Imraj423'

import requests

r = requests.get('http://api.open-notify.org/astros.json')
print(r.text)

s = requests.get('http://api.open-notify.org/iss-now.json')
print(r.text)


# if __name__ == '__main__':
#     main()
