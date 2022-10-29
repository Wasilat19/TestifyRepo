from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.Testifyltd.com")
    hero_element = driver.find_element(By.XPATH, "/html/body/div/main/section[1]/div/div[1]/div[1]/h1")
    print("hero element", hero_element, hero_element.text)
    links = driver.find_elements(By.TAG_NAME, "a")
    for link in links:
        print("link:", link.text)


if __name__ == '__main__':
    main()
