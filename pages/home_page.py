from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
import time

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def scroll_to_end(self):
        # Get the size of the screen
        screen_size = self.driver.get_window_size()
        start_x = screen_size['width'] / 2  # Start in the middle of the screen
        start_y = screen_size['height'] * 0.8  # Start near the bottom of the screen
        end_y = screen_size['height'] * 0.2  # End near the top of the screen

        # Perform the scroll action
        while True:
            # Swipe from start_y to end_y
            TouchAction(self.driver).press(x=start_x, y=start_y).wait(1000).move_to(x=start_x, y=end_y).release().perform()
            # Add a small delay to allow content to load
            time.sleep(1)

            # Check if we have reached the end of the scroll
            if self.driver.find_elements(MobileBy.ACCESSIBILITY_ID, "My lists"):
                break  # Stop scrolling if we find the "My lists" element

    def scroll_to_top(self):
        # Get the size of the screen
        screen_size = self.driver.get_window_size()
        start_x = screen_size['width'] / 2  # Start in the middle of the screen
        start_y = screen_size['height'] * 0.2  # Start near the top of the screen
        end_y = screen_size['height'] * 0.8  # End near the bottom of the screen

        last_article_count = 0  # Initialize the count of articles

        while True:
            # Perform the scroll action
            TouchAction(self.driver).press(x=start_x, y=start_y).wait(1000).move_to(x=start_x, y=end_y).release().perform()
            # Add a small delay to allow content to load
            time.sleep(1)

            # Get the current number of articles displayed
            articles = self.driver.find_elements(MobileBy.CLASS_NAME, "android.widget.TextView")  # Adjust the class name as needed
            current_article_count = len(articles)

            # Check if we have reached the end of the scroll
            if current_article_count == last_article_count:
                break  # Stop scrolling if no new articles are loaded

            last_article_count = current_article_count  # Update the last article count

    def click_my_lists(self):
        my_lists_icon = self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "My lists")
        my_lists_icon.click()

    def click_history(self):
        history_icon = self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "History")
        history_icon.click()

    def click_nearby(self):
        nearby_icon = self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "Nearby")
        nearby_icon.click()

    def click_browse(self):
        browse_icon = self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "Browse")
        browse_icon.click()

    def click_explore(self):
        browse_icon = self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "Explore")
        browse_icon.click()

    def click_search_bar(self):
        # Locate the search bar using its accessibility ID
        search_bar = self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "Search Wikipedia")
        search_bar.click()  # Simulate a click on the search bar

    def enter_search_text(self, text):
        # Locate the search text input using its resource ID
        search_text_input = self.driver.find_element(MobileBy.ID, "org.wikipedia.alpha:id/search_src_text")
        search_text_input.send_keys(text)  # Enter the search text

    def get_search_result(self):
        # Locate the search result using its resource ID
        search_result = self.driver.find_element(MobileBy.ID, "org.wikipedia.alpha:id/fragment_feed_header")
        return search_result  # Return the search result element

    def clear_search_bar(self):
        # Locate the clear search button using its accessibility ID
        clear_button = self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "Clear query")
        clear_button.click()  # Simulate a click to clear the search bar 

    def click_settings(self):
        # Locate the settings icon using its accessibility ID
        settings_icon = self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "Settings")
        settings_icon.click()  # Simulate a click on the settings icon 