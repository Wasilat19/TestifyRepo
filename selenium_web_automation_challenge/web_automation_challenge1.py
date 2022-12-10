"""Using    the    Chrome    browser    navigate    to https://www.facebook.com/
fill  in  the  email/phone  and password text box then click the Login Button.
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def send_keys_to_element(element, *keys):
    element.send_keys(keys)


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.facebook.com")
    send_keys_to_element(driver.find_element(By.NAME, "email"), "wasilat5050@yahoo.com")
    send_keys_to_element(driver.find_element(By.NAME, "pass"), "*****")
    form = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div/div[2]/div')
    form.find_element(By.NAME, "login").click()
    time.sleep(20)


if __name__ == '__main__':
    main()
