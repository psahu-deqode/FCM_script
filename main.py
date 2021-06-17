import time
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
    time.sleep(15)
    token = driver.find_element_by_id("token").text
    list1 = [token]
    with open('event.csv', 'a') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(list1)
        f_object.close()
    WebDriverWait(driver, 3600).until(
        EC.text_to_be_present_in_element((By.ID, "notification"), "title")
    )
    list2 = [token, "received"]
    with open('event_with_status.csv', 'a') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(list2)
    print(driver.find_element_by_id("notification").text)


if __name__ == '__main__':

    for t in range(10):
        t = threading.Thread(target=main)
        t.start()
