import json
import time
import requests
import threading
from _csv import writer
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

option = Options()

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

option.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 1
})
token_list = []


def main():
    driver = webdriver.Chrome(chrome_options=option, executable_path='/usr/bin/chromedriver')
    driver.get('http://localhost:8000/')
    button = driver.find_element_by_id("token_button")
    button.click()
    time.sleep(20)
    token = driver.find_element_by_id("token").text
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'key=AAAAfRVjqX8:APA91bHtxxpFWg33uD4Wj-Vlp915l6WZVjOZrbpkwgTlP5GnIrgLLHnDRlxTcrg9-Y'
                         '-7f95PTR6AB_GwF5BahUtPjsi3_f3aRIrAFXcQH5HoK-B9suEqXPikQr8tLBbgCjnNAR-oGPgR',
        'Content-Type': 'application/json'
    }
    url = 'https://fcm.googleapis.com/fcm/send'
    payload = {
        "registration_ids": [token],
        "collapse_key": "type_a",
        "data": {
            "notification": {
                "title": "Title of Your Notification",
                "body": "Body of Your Notification",
            }
        }

    }
    resp = requests.post(url, headers=headers, data=json.dumps(payload))
    if resp.status_code == 200:
        send_status = "Success"
    else:
        send_status = "Success"
    # if the notification is not received and the browser wait time expires, the received status will be "pending"
    try:
        WebDriverWait(driver, 3600).until(
            EC.text_to_be_present_in_element((By.ID, "notification"), "title")
        )
        received_status = "Received"
    except:
        received_status = "Pending"
    data_list = [token, send_status, received_status]
    with open('event_with_status.csv', 'a') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(data_list)


if __name__ == '__main__':

    for t in range(10):
        t = threading.Thread(target=main)
        t.start()
