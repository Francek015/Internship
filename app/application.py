from pages.main_page import MainPage
# from pages.header import Header
from pages.search_results import SearchResultsPage
# from pages.signin_page import Signin
# from pages.cart_items_page import CartItems
from pages.base_page import Page


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
#         self.header = Header(self.driver)
        self.search_results = SearchResultsPage(self.driver)
#         self.signin_page = Signin(self.driver)
#         self.cart_items_page = CartItems(self.driver)
        self.base_page = Page(self.driver)
