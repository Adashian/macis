import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from webdriver_manager.chrome import ChromeDriverManager

from abstract.selenium_listener import MyListener


@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    options.add_argument('chrome')  #use headless if you don't need a browser UI
    options.add_argument('--start-maximized')
    options.add_argument('--window-size=1024,800')
    return options


@pytest.fixture
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
    return driver


@pytest.fixture(scope='function')
def setup(request, get_webdriver):
    driver = get_webdriver
    driver = EventFiringWebDriver(driver, MyListener())
    url = 'https://www.macys.com/'
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)
    driver.delete_all_cookies()
    yield driver
    driver.quit()
