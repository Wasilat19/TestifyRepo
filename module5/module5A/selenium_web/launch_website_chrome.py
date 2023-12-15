from selenium import webdriver

def main():
    driver = webdriver.Chrome(executable_path=r"C:\Users\SAMSUNG\Documents\Webdrivers\chromedriver_win32/chromedriver.exe")
    driver.get("http://www.google.com")
    driver.close()


main()
