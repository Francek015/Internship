from pages.shop_page import ShopPage
from pages.footer_page import Footer
from pages.search_results import SearchResultsPage
# from pages.signin_page import Signin
# from pages.cart_items_page import CartItems
from pages.base_page import Page


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.shop_page = ShopPage(self.driver)
        self.footer_page = Footer(self.driver)
        self.search_results = SearchResultsPage(self.driver)
#         self.signin_page = Signin(self.driver)
#         self.cart_items_page = CartItems(self.driver)
        self.base_page = Page(self.driver)
