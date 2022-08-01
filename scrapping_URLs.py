from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

ROTTEN_URL = 'https://www.rottentomatoes.com/browse/movies_at_home/sort:popular?page=1'
chrome_driver_path = 'C:\Devs\chromedriver.exe'
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get(ROTTEN_URL)
time.sleep(2)
driver.find_element(by=By.XPATH,
                    value='//*[@id="truste-consent-button"]').click()

# getting every movie URL

for x in range(0, 500):
    time.sleep(2)
    try:
        driver.find_element(by=By.XPATH,
                            value='//*[@id="main-page-content"]/div/div[5]/button').click()
        print('it works', x)

    except:
        pass

with open("C:/Users/Lenovo/Desktop/new_movies_rotten.html") as rotten_page:
    soup = BeautifulSoup(rotten_page, 'html.parser')
    links = []
    for link in soup.findAll('a'):
        links.append(link.get('href'))

print(links)

