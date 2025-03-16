import pytest
import allure
from pages.home_page import HomePage


@allure.feature('Navigation')
class TestNavigation:
    
    @allure.story('Navigate through app sections')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.all
    @pytest.mark.task1
    def test_navigation_flow(self, driver):
        home_page = HomePage(driver)
        home_page.scroll_to_end()  # Ensure this method is implemented
        home_page.click_my_lists()
        # home_page.click_history() # comment out due to bug History Button Closes App 
        # home_page.click_nearby() # comment out due to bug report Nearby Button Closes App
        home_page.click_explore() 
        home_page.scroll_to_top()

