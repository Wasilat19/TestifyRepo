from selenium import webdriver

def main():
    driver = webdriver.Firefox(executable_path=r"C:\Users\SAMSUNG\Documents\Webdrivers\geckodriver-v0.32.0-win64/geckodriver.exe")
    driver.get("http://www.google.com")
    driver.close()


main()
