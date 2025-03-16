import time
import pytest
import allure
from pages.home_page import HomePage
from pages.search_page import SearchPage

@allure.feature('Search Functionality')
class TestSearch:
    
    @allure.story('Search for a location')
    @allure.severity(allure.severity_level.NORMAL) 
    @pytest.mark.search
    @pytest.mark.task2
    @pytest.mark.all
    def test_search_new_york(self, driver):
        home_page = HomePage(driver)
        search_page = SearchPage(driver)

        # Launch the app and click on the search bar
        home_page.click_search_bar()
        time.sleep(3)
        
        # Search for "New York"
        home_page.enter_search_text("New York")
        search_result = home_page.get_search_result()
        
        # Assert that the search bar is expanded with results
        assert search_result != None , "Search result is not displayed."  # Check if the search result is visible

        
        # Close the search
        search_page.close_search() 