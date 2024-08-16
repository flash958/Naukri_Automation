from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from selenium.webdriver.chrome.options import Options

@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    return driver


