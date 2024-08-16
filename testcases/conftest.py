from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from selenium.webdriver.chrome.options import Options

@pytest.fixture()
def setup():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    return driver


