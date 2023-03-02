import booking.constants as const
import os
from selenium import webdriver
import requests
import time

class Booking(webdriver.Chrome):
    def __init__(self,driver_path=r"C:\Users\paulk\Desktop\Selenium\Selenium101", teardown=False): #acces to chromderiver
        self.driver_path = driver_path
        self.teardown=teardown
        os.environ['PATH'] += r"C:\Users\paulk\Desktop\Selenium\Selenium101"
        super(Booking, self).__init__()
        self.implicitly_wait(15) #wait 15 secs, or proceed depending on which comes first
        self.maximize_window()
        

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown: #if teardown is true, then it will shut down, otherwise it will be left on for a while
            self.quit()
    

    def land_first_page(self):
        self.get(const.BASE_URL)
        
        while(True):
            pass
        

    def change_currency(self, currency): #currency as parameter if you want to change to a diff currency
        self.implicitly_wait(5)
        close_button = self.find_element(By.XPATH,"//application[@aria-label='Dismiss sign-in info.']//button")
        close_button.click()
        
        currency_element = self.find_element("id","header-currency-picker-trigger")
        
        currency_element.click()

        