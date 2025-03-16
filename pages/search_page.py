from appium.webdriver.common.mobileby import MobileBy

class SearchPage:
    def __init__(self, driver):
        self.driver = driver

    def search_for(self, query):
        search_bar = self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "Search Wikipedia")
        search_bar.click()
        search_bar.send_keys(query)

    def close_search(self):
        close_button = self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "Clear query")
        close_button.click() 