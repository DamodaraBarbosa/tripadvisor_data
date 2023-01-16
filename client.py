from time import sleep
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
    timeout= 5
)

# insert the info to be searched in the search bar:
scrape.insert_info(
    info= 'Fortaleza', 
    path= '//div[@class="slvrn Z0 Wh EcFTp"]//input[@class= "qjfqs _G B- z _J Cj R0"]',
)

# scrape.click(
#     path= '//div[@id= "onetrust-accept-btn-container"]//button',
#     timeout= 10
# )

sleep(2)

# click in the hotels' tab:
scrape.click(
    path= '//a[@data-tab-name= "Hotéis"]',
    timeout= 15
)

# get all the hotels in the webpage:
hotels = scrape.get_elements(
    path= '//div[@class= "result-title"]',
    timeout= 5
)

data = dict()
datas = list()

for hotel in hotels:
    hotel.click()
    scrape.switch_tab(tab= 1)

    sleep(4)

    prices = scrape.get_elements(path= '//div[@class= "WXMFC b"]', timeout= 10)
    
    prices_list = scrape.info_iterator(prices)
    data['prices'] = prices_list
    
    browser.close()
    scrape.switch_tab(tab= 0)
    
    print(data)

browser.close()
