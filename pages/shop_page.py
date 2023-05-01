from pages.base_page import Page
from selenium.webdriver.common.by import By

class ShopPage(Page):
    POPUP = (By.XPATH, "//div/button[@class = 'popup-close']")

    def open_main(self):
        self.open_url('https://shop.cureskin.com/')


    def open_search_result(self):
        self.open_url('https://shop.cureskin.com/search?q=cure')

    def close_popup(self):
        self.driver.find_element(*self.POPUP).click()








