import requests
import os
import instabot
from dotenv import load_dotenv
from instabot import Bot



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
		print('downloading image id = {}'.format(image_id))
		download_hubble_img(image_id)
		print('OK!')


if __name__ == "__main__":
	load_dotenv()
	login=os.getenv("INSTA_LOGIN")
	password=os.getenv("INSTA_PASS")

	#bot = Bot()
	#bot.login(username=login, password=password)

	image_id = '1'
	collection = 'spacecraft'
	get_hubble_image_id(collection)
	#download_hubble_img(image_id)
	#image_link = get_hubble_img_link(image_id)
	#print(image_link)
	#print(get_file_extension(image_link))
	#fetch_spacex_last_launch()
