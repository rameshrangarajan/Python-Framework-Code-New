import logging
from src.pages import base_page
from src.locators.searchPage_locators import SearchPageLocators as spl


class SearchPage(base_page.Page):
    @base_page.log_func_name
    def return_driver(self):
        return SearchPage(self.driver)

    @base_page.log_func_name
    def enter_search_string(self, search_string):
        logger = logging.getLogger(__name__)
        self.set_field_value(spl.search_input_loc['search_input'], search_string)
        logger.info('%s string entered into search box', search_string)

    @base_page.log_func_name
    def click_search_element(self, element_type, element_name):
        logger = logging.getLogger(__name__)
        self.click_element(spl.__dict__[element_type][element_name])
        logger.info('Element %s from %s clicked successfully', element_name, element_type)

    @base_page.log_func_name
    def get_element_text(self,element_type, element_name):
        element = self.find_element(spl.__dict__[element_type][element_name])
        element_text = element.text
        return element_text

    @base_page.log_func_name
    def is_element_displayed_and_enabled(self, element_type, element_name, fill):
        return fill in self.find_element(spl.__dict__[element_type][element_name]).get_attribute("src")



    @base_page.log_func_name
    def find_all_elements(self, element_type, element_name):
        return self.find_elements(spl.__dict__[element_type][element_name])

    @base_page.log_func_name
    def findelement(self, element_type, element_name, timeout=None):
        try:
            return self.find_element(spl.__dict__[element_type][element_name], timeout)
        except:
            return False

    @base_page.log_func_name
    def enter_text_into_textfield(self, element_type, element_name, text_string):
        logger = logging.getLogger(__name__)
        self.set_field_value(spl.__dict__[element_type][element_name], text_string)
        logger.info('%s string entered into text box', text_string)
