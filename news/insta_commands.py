import os
import time
from keys import insta_username, insta_password, lilmayo_directory


def get_insta_posts(user):

    post_list_rehs = os.listdir(f"{lilmayo_directory}/{user}")

    os.system(f'cd {lilmayo_directory}/news/insta_posts')
    time.sleep(2)
    os.system(f'instagram-scraper {user} -u {insta_username} -p {insta_password} -m 3')

    post_list_new = os.listdir(f"{lilmayo_directory}/{user}")

    new_list = []
    for item in post_list_new:
        if item not in post_list_rehs:
            file_size = os.stat(f"lilmayo/{item}").st_size
            if file_size < 8000000:
                new_list.append(item)
            else:
                print(f"lilmayo file too big for discord ({file_size / 1000000} mb)")
        else:
            pass

    return new_list
