from time import sleep
from selenium.webdriver.support.ui import Select
from pages.base_page import Page
from selenium.webdriver.common.by import By

class SearchResultsPage(Page):
    SEARCH_RESULT = (By.ID, 'ProductCount')
    SORT_BY = (By.XPATH, '//span[@class = "mobile-facets__open button button--small button--full-width"]')
    HIGH_LOW = (By.XPATH, '//option[@value = "price-descending"]')
    PRICE = (By.XPATH, "//ul[@id='product-grid']/li//price-money/bdi")
    RELEVANCE = (By.XPATH, '//div/select')
    CLOSE_TAB = (By.XPATH, '//span[@class= "mobile-facets__close"]')

    def verify_search_result(self, expected_text):
        self.verify_text(expected_text, *self.SEARCH_RESULT)


    def click_sort_by(self):
        self.driver.find_element(*self.SORT_BY).click()
        sleep(1.5)

    def click_relevance(self):
        self.driver.find_element()


    def click_high_to_low(self):
        # self.driver.find_element(*self.HIGH_LOW).click()
        sort_by = self.find_element(*self.RELEVANCE)
        select = Select(sort_by)
        select.select_by_value('price-descending')

        sleep(1.5)
        self.driver.find_element(*self.CLOSE_TAB).click()
        sleep(2.5)


    def verify_order(self):
        products_price_list = self.find_elements(*self.PRICE)
        products_price_list = products_price_list[2::3]
        final_price_list = []

        for price in products_price_list:
            value = float(price.text[3:])
            final_price_list.append(value)

        item_1 = final_price_list[0]
        last_item = final_price_list[-1]
        assert item_1 > last_item, f'{item_1} is not higher than {last_item}, filter test failed'




