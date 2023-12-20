"""Using any browser navigate to any YouTube video of your choice, allow your script to wait
for the comments to load then get the first two comments, and print them in the terminal.
"""

import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def scroll_by_offset(action, delta_y):
    action.scroll_by_amount(0, delta_y).perform()


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.youtube.com/watch?v=VywxIQ2ZXw4")
    action = ActionChains(driver)
    driver.maximize_window()

    scroll_by_offset(action, 400)
    web_driver_wait = WebDriverWait(driver, 5)
    web_driver_wait.until(EC.visibility_of_element_located((By.TAG_NAME, "ytd-comment-renderer")))

    comments = driver.find_elements(By.TAG_NAME, "ytd-comment-renderer")
    for comment in comments:
        comment_content = comment.find_element(By.ID, 'content')
        print(comment_content.text)

    time.sleep(20)


if __name__ == '__main__':
    main()
