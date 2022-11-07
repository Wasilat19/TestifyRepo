import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def send_keys_to_element(element, keys):
    element.send_keys(keys)


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.testifyltd.com/contact")
    send_keys_to_element(driver.find_element(By.NAME, "firstname"), "Wasilat")
    send_keys_to_element(driver.find_element(By.NAME, "lastname"), "Braimah")
    send_keys_to_element(driver.find_element(By.NAME, "email"), "braimahwasilat@gmail.com")
    time.sleep(10)


if __name__ == '__main__':
        main()