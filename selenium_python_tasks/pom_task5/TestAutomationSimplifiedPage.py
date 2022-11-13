from selenium.webdriver.common.by import By


class TestAutomationSimplifiedPage:

    def __init__(self, driver):
        driver.get("https://academy.testifyltd.com/courses/test-automation-simplified")
        self.courses_button = driver.find_element(By.TAG_NAME, 'button')
        self.success_stories = driver.find_element(By.LINK_TEXT, 'Success Stories')
        self.title = driver.find_element(By.TAG_NAME, 'h1')
        self.enroll_button = driver.find_element(By.TAG_NAME, 'span')
