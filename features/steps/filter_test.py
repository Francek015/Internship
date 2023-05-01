from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import when, given, then
from time import sleep


@given('Open cureskin results for cure')
def open_cureskin(context):
    context.app.shop_page.open_search_result()


@when('verify {search_word}')
def verify_results_count(context, search_word):
    context.app.search_results.verify_search_result(search_word)

@when('click sort by')
def click_sort(context):
    context.app.search_results.click_sort_by()
    sleep(3)

@when('click high to low')
def click_high_to_low(context):
    context.app.search_results.click_high_to_low()


@then('Verify order')
def verify_order(context):
    context.app.search_results.verify_order()


