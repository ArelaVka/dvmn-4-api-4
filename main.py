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

if __name__ == "__main__":
    directory = 'images'
    url = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'
    img_name = 'img1.jpeg'
    make_dir(directory)
    download_img(url, img_name, directory)
    
