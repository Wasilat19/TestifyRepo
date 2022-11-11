from selenium.webdriver.common.by import By


class ContactPage:

    def __init__(self, driver):
        driver.get("https://www.testifyltd.com/contact")
        self.message_textbox = driver.find_element(By.NAME, 'message')
        self.email_input = driver.find_element(By.NAME, 'email')
        self.lastname_input = driver.find_element(By.NAME, 'lastname')
        self.firstname_input = driver.find_element(By.NAME, 'firstname')
        self.submit_button = driver.find_element(By.TAG_NAME, 'form').find_element(By.TAG_NAME, 'button')
