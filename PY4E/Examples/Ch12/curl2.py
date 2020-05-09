import urllib.request, urllib.parse, urllib.error

img = urllib.request.urlopen('http://data.pr4e.org/cover.jpg')
fhand = open('cover3.jpg', 'wb')
size = 0
while True:
    info = img.read(10000)
    if len(info) < 1: break
    size += len(info)
    print(size, len(info))
    fhand.write(info)

fhand.close()