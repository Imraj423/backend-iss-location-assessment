__author__ = 'Imraj423'
import urllib


try:
    x = urllib.request.urlopen('https://www.google.com/search?q=test')
    print(x.read())

except Exception as e:
    print(str(e))


if __name__ == '__main__':
    main()
