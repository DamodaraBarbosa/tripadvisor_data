from classes import Webdriver, Scrape
from selenium.webdriver.common.by import By

url = 'https://www.tripadvisor.com.br/'

webdriver = Webdriver(url)
browser = webdriver.set_driver()
browser.get(url)

scrape = Scrape(browser)

scrape.click(
    path= '//div[@id= "onetrust-accept-btn-container"]//button',
    how= By.XPATH
)

scrape.insert_info(
    info= 'Fortaleza', 
    path= '//div[@class="slvrn Z0 Wh EcFTp"]//input[@class= "qjfqs _G B- z _J Cj R0"]',
    how= By.XPATH
)

# browser.close()
