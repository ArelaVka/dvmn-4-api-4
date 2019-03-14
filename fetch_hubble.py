import requests
import os


def get_hubble_img_link(image_id):
    url = 'http://hubblesite.org/api/v3/image/' + str(image_id)
    response_json = requests.get(url).json()
    for n, link in enumerate(response_json["image_files"]):
        img_link = response_json["image_files"][n]["file_url"]
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
    filename = '{}/{}.{}'.format(directory, image_id, ext)
    with open(filename, 'wb') as file:
        file.write(requests.get(url).content)

def get_hubble_image_id(collection):
    images_id = []
    url = 'http://hubblesite.org/api/v3/images/' + collection
    response_json = requests.get(url).json()
    for image in response_json:
        images_id.append(image["id"])
    for image_id in images_id:
        download_hubble_img(image_id)


collection = 'printshop'
get_hubble_image_id(collection)