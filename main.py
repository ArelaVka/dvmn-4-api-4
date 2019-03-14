import os
import instabot
from dotenv import load_dotenv
from instabot import Bot
import glob
from os import listdir
#import fetch_spacex
#import fetch_hubble


def upload_to_instagramm(login, password, picdir):
    try:
        with open('pics.txt', 'r', encoding='utf8') as f:
            posted_pic_list = f.read().splitlines()
    except ValueError:
            posted_pic_list = []

    bot = Bot()
    bot.login(username=login, password=password)

    mypics = listdir(picdir)
    mypics.sort()
    for mypic in mypics:
        full_path_img = './{}/{}'.format(picdir, mypic)
        if full_path_img not in posted_pic_list:
            bot.upload_photo(full_path_img, caption=mypic)
            posted_pic_list.append(full_path_img)
            with open('pics.txt', 'a', encoding='utf8') as f:
                f.write(full_path_img + "\n")

def clear_img_dir(picdir):
    remove_files = glob.glob('./{}/*CONVERTED*'.format(picdir))
    for remove_file in remove_files:
        os.remove(remove_file)


if __name__ == "__main__":

    #load_dotenv()
    #login=os.getenv("INSTA_LOGIN")
    #password=os.getenv("INSTA_PASS")

    picdir = 'images'
    #upload_to_instagramm(login, password, picdir)
    clear_img_dir(picdir)
