#!/usr/bin/env python 

__author__ = 'Imraj423'

import urllib.request
import urllib.parse


url = 'http://api.open-notify.org/astros.json'
f = urllib.request.urlopen(url)
print(f.read().decode('utf-8'))

if __name__ == '__main__':
    main()
