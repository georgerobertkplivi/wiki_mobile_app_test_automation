import pytest
from appium import webdriver
from resources.desired_capabilities import get_desired_capabilities

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Remote("http://localhost:4723/wd/hub", get_desired_capabilities())
    yield driver
    driver.quit()
