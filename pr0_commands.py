from selenium import webdriver
import json
import time

PR0_URL = "https://pr0gramm.com/"
WELTRAUM = "weltraumgedöns"


def get_pr0_posts():
    chrome_driver_path = "/Users/basti/Development/chromedriver"
    driver = webdriver.Chrome(executable_path=chrome_driver_path)

    driver.get(f"{PR0_URL}new/{WELTRAUM}")

    # Finding id's of latest posts
    uploads = []
    all_uploads = driver.find_elements_by_class_name("stream-row a")
    for item in all_uploads:
        id_name = item.get_attribute(name="id").split("-")[1]
        uploads.append(id_name)

    # Loading rehposts from json
    url_list = []
    with open("reh.json") as reh_file:
        reh_data = json.load(reh_file)
        temp = reh_data["rehs"]
        new_ids = []
        for upload in uploads:
            if upload not in temp:
                driver.get(f"{PR0_URL}new/{WELTRAUM}/{upload}")
                time.sleep(3)
                media = driver.find_element_by_class_name("item-image-actual")
                media_url = media.get_attribute("src")
                new_ids.append(upload)
                url_list.append(media_url)

    driver.quit()

    # Saving new posts to rehposts
    for n in range(len(new_ids)):
        data_to_save = {
            "rehs": new_ids[n]
        }
        temp.append(data_to_save["rehs"])
        with open("reh.json", "w") as reh_file:
            json.dump(reh_data, reh_file)

    return url_list
