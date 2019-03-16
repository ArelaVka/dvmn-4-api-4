import os
import instabot
from dotenv import load_dotenv
from instabot import Bot
import glob
from os import listdir
from fetch_spacex import fetch_spacex_last_launch
from fetch_hubble import get_hubble_image_id


def upload_to_instagram(login, password, pic_dir):
    try:
        with open('pics.txt', 'r', encoding='utf8') as f:
            posted_pic_list = f.read().splitlines()
    except FileNotFoundError:
            posted_pic_list = []

    bot = Bot()
    bot.login(username=login, password=password)

    mypics = listdir(pic_dir)
    mypics.sort()
    for mypic in mypics:
        full_path_img = './{}/{}'.format(pic_dir, mypic)
        if full_path_img in posted_pic_list:
            continue
        bot.upload_photo(full_path_img, caption=mypic)
        posted_pic_list.append(full_path_img)
        with open('pics.txt', 'a', encoding='utf8') as f:
            f.write(full_path_img + "\n")

def clear_img_dir(pic_dir):
    remove_files = glob.glob('./{}/*CONVERTED*'.format(pic_dir))
    for remove_file in remove_files:
        os.remove(remove_file)


if __name__ == '__main__':

    pic_dir = 'images'
    fetch_spacex_last_launch(pic_dir)
    collection = 'printshop'
    get_hubble_image_id(collection, pic_dir)

    load_dotenv()
    login=os.getenv("INSTA_LOGIN")
    password=os.getenv("INSTA_PASS")
    upload_to_instagram(login, password, pic_dir)
    clear_img_dir(pic_dir)
