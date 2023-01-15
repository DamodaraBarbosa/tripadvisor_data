from classes import Webdriver, Scrape
from selenium.webdriver.common.by import By

url = 'https://www.tripadvisor.com.br/'

webdriver = Webdriver(url)
browser = webdriver.set_driver()
browser.get(url)

scrape = Scrape(browser)

# close the disclaimer:
scrape.click(
    path= '//div[@id= "onetrust-accept-btn-container"]//button',
)

# insert the info to be searched in the search bar:
scrape.insert_info(
    info= 'Fortaleza', 
    path= '//div[@class="slvrn Z0 Wh EcFTp"]//input[@class= "qjfqs _G B- z _J Cj R0"]',
)

# click in the hotels' tab:
scrape.click(
    path= '//a[@data-tab-name= "Hotéis"]',
    timeout= 10
)

# get all the hotels in the webpage:
hotels = scrape.get_elements(
    path= '//div[@class= "result-title"]'
)

print(hotels)

# browser.close()
