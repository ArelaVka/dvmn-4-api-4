import requests

filename = 'HST-SM4.jpeg'
url = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/'

response = requests.get(url)
with open(filename, 'wb') as file:
    file.write(response.content)
