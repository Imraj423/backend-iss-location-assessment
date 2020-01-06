__author__ = 'Imraj423'

import urllib.request
import urllib.parse


def main():
    url = 'http://api.open-notify.org/astros.json'
    f = urllib.request.urlopen(url)
    print(f.read().decode('utf-8'))


if __name__ == '__main__':
    main()
