"""Navigate any browser to https: // weather.com /, get the current temperature and print it out in the terminal.
Then print out the temperature for Morning, Afternoon, Evening,and Overnight
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://weather.com/")
    current_temp_value = driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/main[1]/div[2]/main[1]/div[1]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/span[1]')
    print("Current Temperature:", current_temp_value, current_temp_value.text)
    morning_temp_value = driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/main[1]/div[2]/main[1]/div[3]/section[1]/div[1]/ul[1]/li[1]/a[1]/div[1]/span[1]')
    print("Morning Temperature:", morning_temp_value, morning_temp_value.text)
    afternoon_temp_value = driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/main[1]/div[2]/main[1]/div[3]/section[1]/div[1]/ul[1]/li[2]/a[1]/div[1]/span[1]')
    print("Afternoon Temperature:", afternoon_temp_value, afternoon_temp_value.text)
    evening_temp_value = driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/main[1]/div[2]/main[1]/div[3]/section[1]/div[1]/ul[1]/li[3]/a[1]/div[1]/span[1]')
    print("Evening Temperature:", evening_temp_value, evening_temp_value.text)
    night_temp_value = driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/main[1]/div[2]/main[1]/div[3]/section[1]/div[1]/ul[1]/li[4]/a[1]/div[1]/span[1]')
    print("Night Temperature:", night_temp_value, night_temp_value.text)
    time.sleep(10)


if __name__ == '__main__':
    main()
