import requests
import os

def fetch_spacex_last_launch():
  url = 'https://api.spacexdata.com/v3/launches/latest'
  directory = 'images'
  if not os.path.exists(directory):
        os.makedirs(directory)
  response_json = requests.get(url).json()
  img_links = response_json["links"]["flickr_images"]
  for n, img_link in enumerate(img_links, 1):
    filename = '{}/spacex{}.jpg'.format(directory, n)
    with open(filename, 'wb') as file:
        file.write(requests.get(img_link).content)
        
     
if __name__ == "__main__":
    fetch_spacex_last_launch()
