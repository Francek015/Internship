from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from app.application import Application

def browser_init(context):
    """
    :param context: Behave context
    """
    # service = Service('./chromedriver.exe')
    # service = Service('./geckodriver.exe')
    # context.driver = webdriver.Chrome(service=service)
    # context.driver = webdriver.Firefox(service=service)
    # # context.browser = webdriver.Safari()
    # # context.browser = webdriver.Firefox()
    #
    # context.driver.maximize_window()
    # context.driver.implicitly_wait(4)
    # context.app = Application(driver=context.driver)

    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # context.driver = webdriver.Chrome(
    #     chrome_options=options,
    #     service=service
    # )
    # context.app = Application(driver=context.driver)
    #
    #
    desired_cap = {
        'browser': 'Chrome',
        'os_version': '11',
        'os': 'Windows',

    }

    bs_user = 'stjepanrogina_JNSTs4'
    bs_key = 'pwK8y9SWn2qqsXszE1yU'
    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.app = Application(driver=context.driver)



def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
