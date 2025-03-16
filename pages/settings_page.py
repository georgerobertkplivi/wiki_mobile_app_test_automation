from appium.webdriver.common.mobileby import MobileBy
import time

from pages.base_page import BasePage


class SettingsPage(BasePage):
    SHOW_IMAGE_TOOGLE = 'new UiSelector().resourceId("org.wikipedia.alpha:id/switchWidget").instance(0)'
    SHOW_LINK_PREVIEW_TOOGLE = 'new UiSelector().resourceId("org.wikipedia.alpha:id/switchWidget").instance(1)'
    SEND_USAGE_REPORT_TOOGLE = 'new UiSelector().resourceId("org.wikipedia.alpha:id/switchWidget").instance(2)'
    SEND_CRASH_REPORT_TOOGLE = 'new UiSelector().resourceId("org.wikipedia.alpha:id/switchWidget").instance(3)'

    def __init__(self, driver):
        self.driver = driver

    def open_settings(self):
        # Click on the ellipses button to open the menu
        ellipses_button = self.driver.find_element(MobileBy.XPATH, "//android.widget.TextView[@content-desc='More options']")
        ellipses_button.click()
        self.wait_seconds(5)

        # Wait for the settings option to show and click on it
        SETTINGS = 'new UiSelector().resourceId("org.wikipedia.alpha:id/explore_overflow_settings")'
        self.wait_until_element_is_present(MobileBy.ANDROID_UIAUTOMATOR, SETTINGS)
        settings_option = self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, SETTINGS)
        self.wait_seconds(5)
        settings_option.click()
        self.wait_seconds(5)


    def click_setting_option(self, xpath):
        # Wait until the setting option is present before clicking
        if self.wait_until_element_is_present(MobileBy.ANDROID_UIAUTOMATOR, xpath):
            setting_option = self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, xpath)
            
            # Check if the toggle is ON or OFF
            toggle_state = setting_option.get_attribute("checked")  # Assuming the toggle has a 'checked' attribute
            if toggle_state == "true":
                print(f"The setting is currently ON for XPath: {xpath}")
            else:
                print(f"The setting is currently OFF for XPath: {xpath}")
                setting_option.click()  # Click to turn it ON if it's OFF
            
            time.sleep(5)  # Wait for 3 seconds after clicking
        else:
            print(f"Setting option not found for XPath: {xpath}")

    def disable_all_settings(self):

        # Click on the specified elements in order
        self.click_setting_option( self.SHOW_IMAGE_TOOGLE)
        self.click_setting_option(self.SHOW_LINK_PREVIEW_TOOGLE)
        self.click_setting_option(self.SEND_USAGE_REPORT_TOOGLE)
        self.click_setting_option(self.SEND_CRASH_REPORT_TOOGLE)

        # Click the "Navigate up" button to go back to the home page
        go_back_button = self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "Navigate up")
        go_back_button.click()