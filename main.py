import urllib.request

image = urllib.request.urlopen('https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg').read()
f = open('img1.jpg', 'wb')
f.write(image)
f.close()
