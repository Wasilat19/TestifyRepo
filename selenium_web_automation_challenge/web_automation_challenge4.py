"""Navigate to https://www.bbc.com/ and print out the top 10 latest news from the home page.
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(" https://www.bbc.com/")
    driver.maximize_window()
    bbc_news1_link = driver.find_element(By.XPATH, '//*[@id="page"]/section[3]/div/ul/li[1]/div/a')
    bbc_news2_link = driver.find_element(By.XPATH, '//*[@id="page"]/section[3]/div/ul/li[2]/div/a')
    bbc_news3_link = driver.find_element(By.XPATH, '//*[@id="page"]/section[3]/div/ul/li[3]/div/a')
    bbc_news4_link = driver.find_element(By.XPATH, '//*[@id="page"]/section[3]/div/ul/li[4]/div/a')
    bbc_news5_link = driver.find_element(By.XPATH, '//*[@id="page"]/section[3]/div/ul/li[5]/div/a')
    bbc_news6_link = driver.find_element(By.XPATH, '//*[@id="page"]/section[4]/div/div/div[2]/div/section[1]/div/ul/li[1]/div/a')
    bbc_news7_link = driver.find_element(By.XPATH, '//*[@id="page"]/section[4]/div/div/div[2]/div/section[1]/div/ul/li[2]/div/a')
    bbc_news8_link = driver.find_element(By.XPATH, '//*[@id="page"]/section[4]/div/div/div[2]/div/section[1]/div/ul/li[3]/div/a')
    bbc_news9_link = driver.find_element(By.XPATH, '//*[@id="page"]/section[4]/div/div/div[2]/div/section[2]/div/ul/li[1]/div/a')
    bbc_news10_link = driver.find_element(By.XPATH, '//*[@id="page"]/section[4]/div/div/div[2]/div/section[2]/div/ul/li[2]/div/a')

    print("BBC News1 Link:", bbc_news1_link.text)
    print("BBC News2 Link:", bbc_news2_link.text)
    print("BBC News3 Link:", bbc_news3_link.text)
    print("BBC News4 Link:", bbc_news4_link.text)
    print("BBC News5 Link:", bbc_news5_link.text)
    print("BBC News6 Link:", bbc_news6_link.text)
    print("BBC News7 Link:", bbc_news7_link.text)
    print("BBC News8 Link:", bbc_news8_link.text)
    print("BBC News9 Link:", bbc_news9_link.text)
    print("BBC News10 Link:", bbc_news10_link.text)
    time.sleep(10)


if __name__ == '__main__':
    main()
