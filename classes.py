from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class Webdriver:
    def __init__(self, url: str) -> None:
        self.url = url
    
    def set_driver(self):
        """""""""
        Set the webdriver that will be used in scraping.
        """""""""
        return webdriver.Chrome()
    
    # def open_url_page(self, webdriver):
    #     """""""""
    #     Uses the webdriver to open the browser at the desired url.
    #     """""""""
    #     return webdriver.get(self.url)

class Scrape:
    """""""""
    Class with methods to scrape the website.
    """""""""
    def __init__(self, webdriver) -> None:
        """""""""
        The attributes:
        * webdriver: the selected webdriver that is selected to work.
        """""""""
        self.webdriver = webdriver

    def click(self, path: str, how: By = By.XPATH , timeout: int = 3):
        """""""""
        Method to click in page's elements. 
        * path: class name, tag name or XPATH;
        * how: set how locate the element in page (CLASS_NAME, TAG_NAME, CSS_SELECTOR or XPATH),
        default = By.XPATH;
        * timeout = set the time until execute the method, default= 3.
        """""""""
        button = WebDriverWait(self.webdriver, timeout).until(
            EC.presence_of_element_located((By.XPATH, path))
        )
        button.click()

    def insert_info(self, info: str, path: str, how: By = By.XPATH, timeout: int = 3):
        """""""""
        * info: the information that is wanted to insert.
        * path: class name, tag name or XPATH;
        * how: set how locate the element in page (CLASS_NAME, TAG_NAME, CSS_SELECTOR or XPATH),
        default = By.XPATH;
        * timeout = set the time (seconds) until execute the method, default= 3.
        """""""""
        search = WebDriverWait(self.webdriver, timeout).until(
            EC.presence_of_element_located((how, path))
        )
        search.send_keys(info) # insert info.
        search.send_keys(Keys.ENTER) # ENTER to set the info in search bar.

    def get_element(self, path: str, how: By = By.XPATH, timeout: int = 3):
        """""""""
        Return the element in the path.
        * path: class name, tag name or XPATH;
        * how: set how locate the element in page (CLASS_NAME, TAG_NAME, CSS_SELECTOR or XPATH),
        default = By.XPATH;
        * timeout = set the time (seconds) until execute the method, default= 3.
        """""""""
        element = WebDriverWait(self.webdriver, timeout).until(
            EC.presence_of_element_located((how, path))
        )
        return element.find_element(how, path)
    
    def get_elements(self, path: str, how: By = By.XPATH, timeout: int = 3):
        """""""""
        Returns an array with all elements in the path.
        * path: class name, tag name or XPATH;
        * how: set how locate the element in page (CLASS_NAME, TAG_NAME, CSS_SELECTOR or XPATH),
        default = By.XPATH;
        * timeout = set the time (seconds) until execute the method, default= 3.
        """""""""
        elements = WebDriverWait(self.webdriver, timeout).until(
            EC.presence_of_element_located((how, path))
        )
        return elements.find_elements(how, path)
    
    def switch_tab(self, tab: int):
        """""""""
        Switch tabs openened in the browser.
        * tab: selects the tab to which it should be switched.
        * close: close the current tab and returns to the previous tab, defalt = True
        """""""""
        self.webdriver.switch_to.window(self.webdriver.window_handles[tab])

        # if close == True:
        #     self.webdriver.close() # close the current tab.
        #     self.webdriver.switch_to.window(self.webdriver.window_handles[tab-1]) # returns to the previous tab.
        # else:
        #     pass
    
    def info_iterator(self, infos: list):
        """""""""
        """""""""
        infos_list = list()

        try:
            for info in infos:
                info = info.text
                infos_list.append(info)
        except TimeoutException:
            pass

        return infos_list

    # def get_data(self, info: str, timeout: int = 3):
    #     # data = WebDriverWait(self.webdriver, timeout).until(
    #     #     EC.presence_of_element_located((how, path))
    #     # )
    #     sleep(timeout)
    #     return info.text
    





