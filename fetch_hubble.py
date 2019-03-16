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

def download_hubble_img(image_id, pic_dir):
    os.makedirs(pic_dir, exist_ok=True)
    url = get_hubble_img_link(image_id)
    ext = get_file_extension(url)
    filename = '{}/{}.{}'.format(pic_dir, image_id, ext)
    with open(filename, 'wb') as file:
        file.write(requests.get(url).content)

def get_hubble_image_id(collection, pic_dir):
    images_id = []
    url = 'http://hubblesite.org/api/v3/images/' + collection
    response_json = requests.get(url).json()
    for image in response_json:
        images_id.append(image["id"])
    for image_id in images_id:
        download_hubble_img(image_id, pic_dir)


if __name__ == '__main__':
    pic_dir = 'images'
    collection = 'printshop'
    get_hubble_image_id(collection, pic_dir)