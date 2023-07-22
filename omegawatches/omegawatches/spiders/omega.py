import scrapy
import json
#from selenium.webdriver import Chrome
from selenium import webdriver
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait



class OmegaSpider(scrapy.Spider):
    name = "omega"
    allowed_domains = ["omegawatches.com"]
    

    def start_requests(self):
        start_url = "https://www.omegawatches.com/en-us/watchfinder"
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
            
        request = SeleniumRequest(
            url=start_url, 
            callback=self.load_all_watches, 
            wait_time=2, 
            script='window.scrollTo(0, document.body.scrollHeight);'
        )
        yield request
        # yield SeleniumRequest(url=start_url, 
        #                       callback=self.parse_watchfinder, 
        #                       wait_time=2, 
        #                       script='window.scrollTo(0, document.body.scrollHeight);'
        #                      )
        
    def load_all_watches(self, response):
        driver = response.meta['driver']
        previous_url = response.url
        loader_element = driver.find_element(By.XPATH, '//div[@class="product-list-pager"]')
      
        while True:
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            # driver.execute_script("arguments[0].scrollIntoView(false);", loader_element)
            WebDriverWait(driver,10).until(EC.url_changes(previous_url))
            current_url = driver.current_url
            
            if current_url == previous_url:
                break
            else: 
                previous_url = current_url
                
    
        print(current_url)
        yield
        
        
        # actions = ActionChains(driver)
        # actions.scroll
        
        
        # actions.send_keys(Keys.END).perform()
