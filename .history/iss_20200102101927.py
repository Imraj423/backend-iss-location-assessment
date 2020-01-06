__author__ = 'Imraj423'
import urllib
import urllib.request


def main():
    try:
        x = urllib.request.urlopen('http://api.open-notify.org/astros.json')
        print(x.read())

    except Exception as e:
        print(str(e))


if __name__ == '__main__':
    main()
