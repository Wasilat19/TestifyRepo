from selenium.webdriver.common.by import By


class SwitchToSoftwareTestingPage:

    def __init__(self, driver):
        driver.get("https://academy.testifyltd.com/courses/switch-to-software-testing")
        self.courses_button = driver.find_element(By.TAG_NAME, 'button')
        self.success_stories = driver.find_element(By.LINK_TEXT, 'Success Stories')
        self.title = driver.find_element(By.TAG_NAME, 'h1')
        self.enroll_button = driver.find_element(By.TAG_NAME, 'span')
        self.faq_button = driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/main[1]/section[1]/div[1]/div[1]/div[2]/div[1]/button[2]/span[1]')

