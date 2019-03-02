import requests
import os

def make_dir(name_of_dir):
    if not os.path.exists(name_of_dir):
        os.makedirs(name_of_dir)

def download_img(url, img_name, directory):
    filename = '{}/{}'.format(directory, img_name)
    response = requests.get(url)
    with open(filename, 'wb') as file:
        file.write(response.content)

def get_img_url(url):
  response = requests.get(url).json()
  return response["links"]["flickr_images"]


if __name__ == "__main__":
    directory = 'images'
    make_dir(directory)
    #url = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'
    #img_name = 'img1.jpeg'
    #download_img(url, img_name, directory)
    url = 'https://api.spacexdata.com/v3/launches/latest'
    #print(get_img_url(url))
    for n, img_url in enumerate(get_img_url(url), 1):
      download_img(img_url, 'spacex{}.jpg'.format(n), directory)
