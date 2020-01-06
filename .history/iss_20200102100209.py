#!/usr/bin/env python 

__author__ = 'Imraj423'

import httpie

r = requests.get('http://api.open-notify.org/astros.json')
r.json()


if __name__ == '__main__':
    main()
