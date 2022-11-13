import time
from selenium import webdriver
from TestAutomationSimplifiedPage import TestAutomationSimplifiedPage
from SwitchToSoftwareTesting import SwitchToSoftwareTestingPage
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    test_automation_simplified = TestAutomationSimplifiedPage(driver)
    switch_to_software_testing = SwitchToSoftwareTestingPage(driver)
    print(test_automation_simplified.courses_button, test_automation_simplified.success_stories)
    print(switch_to_software_testing.title.text, switch_to_software_testing.faq_button)
    time.sleep(20)


if __name__ == '__main__':
    main()
