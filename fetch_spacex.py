import requests
import os


def fetch_spacex_last_launch(pic_dir):
    url = 'https://api.spacexdata.com/v3/launches/latest'
    os.makedirs(pic_dir, exist_ok=True)
    response_json = requests.get(url).json()
    img_links = response_json["links"]["flickr_images"]
    for n, img_link in enumerate(img_links, 1):
        filename = '{}/spacex{}.jpg'.format(pic_dir, n)
        with open(filename, 'wb') as file:
            file.write(requests.get(img_link).content)

if __name__ == '__main__':
    pic_dir = 'images'
    fetch_spacex_last_launch(pic_dir)