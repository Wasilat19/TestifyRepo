from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def locate_by_link_text(driver):
    academy_link = driver.find_element(By.LINK_TEXT, "Academy")
    print("Academy Link:", academy_link)
    hire_link = driver.find_element(By.LINK_TEXT, "Hire")
    print("Hire link:", hire_link)


def locate_by_partial_link_text(driver):
    academy_link = driver.find_element(By.PARTIAL_LINK_TEXT, "adem")
    print("Academy Link/partial:", academy_link)
    test_links = driver.find_elements(By.PARTIAL_LINK_TEXT, "Test")
    print("Test link size:", len(test_links))
    for test_link in test_links:
        print("A Test Link:", test_link)


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.testifyltd.com/contact")
    # locate_by_link_text(driver)
    locate_by_partial_link_text(driver)


if __name__ == '__main__':
    main()
