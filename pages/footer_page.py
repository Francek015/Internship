from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.common.keys import Keys


class Footer(Page):
    EMAIL_INPUT = (By.ID, 'ContactFooter-email')
    SUBMIT_EMAIL = (By.XPATH, "//button[@aria-label= 'Subscribe']")
    EMAIL_SUCCESS = (By.ID, 'ContactFooter-success')


    def input_email_text(self, text):
        self.input_text(text, *self.EMAIL_INPUT)

    def submit_email(self):
        self.driver.find_element(*self.SUBMIT_EMAIL).click()

    def clear_email_field(self):
        self.driver.find_element(*self.SUBMIT_EMAIL).click()
        self.driver.find_element(*self.SUBMIT_EMAIL).send_keys(Keys.CONTROL + 'a')
        self.driver.find_element(*self.SUBMIT_EMAIL).send_keys(Keys.DELETE)

    def verify_email_confirmation(self, expected_text):
        self.verify_text(expected_text, *self.EMAIL_SUCCESS)