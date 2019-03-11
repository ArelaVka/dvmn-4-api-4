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
  
def get_hubble_img_link(image_id):
  url = 'http://hubblesite.org/api/v3/image/' + image_id
  response_json = requests.get(url).json()
  for num, link in enumerate(response_json["image_files"]):
    img_link = response_json["image_files"][num]["file_url"]
  return img_link

def get_file_extension(image_link):
  ext = image_link.split('.')
  return ext[-1]

def download_hubble_img(image_id):
  directory = 'images'
  if not os.path.exists(directory):
        os.makedirs(directory)
  url = get_hubble_img_link(image_id)
  ext = get_file_extension(url)
  filename = '{}.{}'.format(image_id, ext)
  with open(filename, 'wb') as file:
        file.write(requests.get(url).content)


if __name__ == "__main__":
  image_id = '1'
  download_hubble_img(image_id)
  #image_link = get_hubble_img_link(image_id)
  #print(image_link)
  #print(get_file_extension(image_link))
  #fetch_spacex_last_launch()
