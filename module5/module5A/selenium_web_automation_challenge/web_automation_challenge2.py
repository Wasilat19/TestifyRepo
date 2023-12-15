"""Using the firefox browser navigate to https://www.google.com/, enter the text Python in the search box,  then  send  the  Enter  key.
Get the text from the Wikipedia brief on the right side and print the value in the console.
"""

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


def send_keys_to_element(element, *keys):
    element.send_keys(keys)


def main():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.get("http://www.google.com")
    send_keys_to_element(driver.find_element(By.TAG_NAME, 'input'), "Python")
    driver.find_element(By.XPATH, '//body/div[1]/div[3]/form[1]/div[1]/div[1]/div[4]/center[1]/input[1]').send_keys(Keys.ENTER)
    time.sleep(10)
    wikipedia_text = driver.find_element(By.XPATH, '//*[@id="kp-wp-tab-overview"]/div[1]/div/div/div/div/div/div/div[1]/div/div/div/span[1]')
    print(wikipedia_text.text)
    time.sleep(2)
    driver.close()


if __name__ == '__main__':
    main()
