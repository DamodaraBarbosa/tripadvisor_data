from time import sleep
from classes import Webdriver, Scrape
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException

url = 'https://www.tripadvisor.com.br/'

webdriver = Webdriver(url)
browser = webdriver.set_driver()
browser.get(url)

scrape = Scrape(browser)

# close the disclaimer:
scrape.click(
    path= '//div[@id= "onetrust-accept-btn-container"]//button',
    timeout= 10
)

# insert the info to be searched in the search bar:
scrape.insert_info(
    info= 'Fortaleza, Ceará', 
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

    name = scrape.get_element(path= '//h1[@class= "QdLfr b d Pn"]', timeout= 5).text
    data['hotel_name'] = name

    address = scrape.get_element(path= '//span[@class= "fHvkI PTrfg"]', timeout= 5).text
    data['address'] = address

    sleep(2)

    assessment = scrape.get_element(path= '//span[@class= "uwJeR P"]', timeout= 5).text
    data['assessment'] = assessment

    number_reviews = scrape.get_element(path= '//span[@class= "hkxYU q Wi z Wc"]', timeout= 5).text
    data['number_reviews'] = number_reviews

    try:
        pedestrian = scrape.get_element(path= '//span[@class= "iVKnd fSVJN"]', timeout= 5).text
        data['pedestrian'] = pedestrian
    except (TimeoutException, StaleElementReferenceException) as exceptions:
        data['pedestrian'] = None
        pass
    
    try:
        restaurants = scrape.get_element(path= '//span[@class= "iVKnd Bznmz"]', timeout= 5).text
        data['restaurants'] = restaurants
    except (TimeoutException, StaleElementReferenceException) as exceptions:
        data['restaurants'] = None
        pass
    
    try:
        attractions = scrape.get_element(path= '//span[@class= "iVKnd rYxbA"]', timeout= 5).text
        data['attractions'] = attractions
    except (TimeoutException, StaleElementReferenceException) as exceptions:
        data['attractions'] = None
        pass

    # services_amenities = scrape.get_elements(
    #     path= '//div[@class= "OsCbb K"]//div[@class= "yplav f ME H3 _c"]', 
    #     timeout= 10
    # )
    # services_amenities_list = scrape.info_iterator(infos= services_amenities)
    # data['services_amenities'] = services_amenities_list

    # amenities = scrape.get_elements(
    #     path= '//div[@data-test-target= "hr-about-group-room_amenities"]', 
    #     timeout= 10
    # )
    # amenities_list = scrape.info_iterator(infos= services)
    # data['amenities'] = amenities_list

    try:
        prices = scrape.get_elements(path= '//div[@class= "WXMFC b"]', timeout= 10)
        prices_list = scrape.info_iterator(prices)
        data['prices'] = prices_list
    except (TimeoutException, StaleElementReferenceException) as exceptions:
        data['prices'] = None
        pass
    
    browser.close()
    scrape.switch_tab(tab= 0)
    
    print(data)

browser.close()
