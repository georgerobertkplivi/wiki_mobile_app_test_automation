from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def find_element(self, locator_type, locator):
        return self.wait.until(
            EC.presence_of_element_located((locator_type, locator))
        )

    def wait_until_element_is_present(self, locator_type, locator):
        """Wait until the specified element is present in the DOM."""
        try:
            self.wait.until(EC.presence_of_element_located((locator_type, locator)))
            return True  # Element is present
        except Exception as e:
            print(f"Element not found: {e}")
            return False  # Element is not present

    def scroll_down(self):
        self.driver.swipe(470, 1400, 470, 150, 800)

    def scroll_up(self):
        self.driver.swipe(470, 150, 470, 1400, 800)

    def wait_seconds(self, seconds):
        import time
        time.sleep(seconds) 