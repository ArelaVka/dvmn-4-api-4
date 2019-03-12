import requests
import os
import instabot
from dotenv import load_dotenv
from instabot import Bot
import glob
import time
from os import listdir


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
			print('downloading image from SpaceX: {}'.format(filename))
			file.write(requests.get(img_link).content)
			print('OK!')
  
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
		print('downloading image from hubble by id: {}'.format(image_id))
		download_hubble_img(image_id)
		print('OK!')


def clear_img_dir(picdir):
	remove_files = glob.glob('./' + picdir + '/*CONVERTED*')
	print(remove_files)
	for remove_file in remove_files:
		os.remove(remove_file)


if __name__ == "__main__":

	collection = 'news'

	#fetch_spacex_last_launch()

	#get_hubble_image_id(collection)


	try:
		with open('pics.txt', 'r', encoding='utf8') as f:
			posted_pic_list = f.read().splitlines()
	except Exception:
			posted_pic_list = []

	load_dotenv()
	login=os.getenv("INSTA_LOGIN")
	password=os.getenv("INSTA_PASS")
	#print(login)
	#print(password)

	bot = Bot()
	bot.login(username=login, password=password)

	picdir = 'images'
	mypics = listdir(picdir)
	mypics.sort()
	for mypic in mypics:
		full_path_img = './{}/{}'.format(picdir, mypic)
		if full_path_img not in posted_pic_list:
			print(full_path_img)
			bot.upload_photo(full_path_img, caption=mypic)
			posted_pic_list.append(full_path_img)
			with open('pics.txt', 'a', encoding='utf8') as f:
				f.write(full_path_img + "\n")

	clear_img_dir(picdir)
	