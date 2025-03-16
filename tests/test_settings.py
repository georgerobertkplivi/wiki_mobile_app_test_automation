import pytest
import allure
from pages.home_page import HomePage
from pages.settings_page import SettingsPage


@allure.feature('Settings Functionality')
class TestSettings:
    
    @allure.story('Disable all settings options')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.task3
    @pytest.mark.all
    def test_disable_settings(self, driver):
        home_page = HomePage(driver)
        settings_page = SettingsPage(driver)

        # Click on settings icon
        settings_page.open_settings()
        
        # Disable all settings options
        settings_page.disable_all_settings()