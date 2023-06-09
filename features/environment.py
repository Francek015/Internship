from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from app.application import Application
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def browser_init(context):
    """
    :param context: Behave context
    """
    # service = ChromeService(ChromeDriverManager().install())
    # # service = Service('./geckodriver.exe')
    # context.driver = webdriver.Chrome(service=service)
    # context.driver = webdriver.Firefox(service=service)
    # # context.browser = webdriver.Safari()

    # context.driver.maximize_window()
    # context.driver.implicitly_wait(4)
    # context.app = Application(driver=context.driver)

    # Chrome headless

    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # context.driver = webdriver.Chrome(
    #     chrome_options=options,
    #     service=service
    # )

    # Firefox headless

    # firefox_options = Options()
    # firefox_options.add_argument("--headless")
    # context.driver = webdriver.Chrome(
    #     service=Service('./geckodriver.exe'),
    #     options=firefox_options)
    #
    #
    #
    #
    # context.app = Application(driver=context.driver)
    #

    # Browser Stack

    # desired_cap = {
    #     'browser': 'Chrome',
    #     'os_version': '10',
    #     'os': 'Windows',
    #
    # }

    # desired_cap = {
    #     'bstack:options': {
    #         "os": "OS X",
    #         "osVersion": "Ventura",
    #         "browserVersion": "16.0",
    #         "local": "false",
    #         "seleniumVersion": "3.14.0",
    #     },
    #     "browserName": "Safari",
    # }
    #
    # bs_user = 'stjepanrogina_JNSTs4'
    # bs_key = 'pwK8y9SWn2qqsXszE1yU'
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    # context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)
    #
    chrome_options = ChromeOptions()
    mobile_emulation = {"deviceName": "iPhone 12 Pro"}
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    context.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=chrome_options)

    # context.driver = webdriver.Chrome(service=service)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.app = Application(driver=context.driver)

    # Allure tests
    # behave - f allure_behave.formatter: AllureFormatter - o test_results / features / tests

    # mobile_emulation = {
    #
    #     "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
    #
    #     "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"}
    #

    #
    # opt = Options()
    # opt.add_experimental_option("debuggerAddress", "localhost:8989")
    # driver = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=opt)
    # driver.get("http://google.com")

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
