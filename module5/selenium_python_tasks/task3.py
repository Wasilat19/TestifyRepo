import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def print_element_fields(element):
    print("Text:", element.text)
    print("Size:", element.size)
    print("Tag name:", element.tag_name)
    print("Location:", element.location)
    print("accessible name:", element.accessible_name)
    print("id:", element.id)
    print("rectangle:", element.rect)


def print_element_properties(element):
    print("Checked state:", element.get_property("checked"))


def print_element_attribute(element):
    print("ID:", element.get_attribute("id"))
    print("Class:", element.get_attribute("class"))
    print("Style:", element.get_attribute("style"))
    print("Inner Text:", element.get_attribute("inner Text"))
    print("Inner HTML:", element.get_attribute("inner HTML"))


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://academy.testifyltd.com/")
    element = driver.find_element(By.XPATH, '//*[@id="__next"]/section/div/div[2]/div[2]')
    testify_link = driver.find_element(By.XPATH, '//*[@id="__next"]/section/div/div[2]/div[2]')
    testify_limited = driver.find_element(By.XPATH, '//*[@id="__next"]/section/div/div[2]/div[2]')
    print_element_properties(testify_limited)
    print_element_attribute(testify_link)
    print_element_fields(element)

    time.sleep(5)


if __name__ == '__main__':
    main()
