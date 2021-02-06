import logging
from src.pages import base_page
from src.locators.googleSearchPage_locators import GoogleSearchPageLocators as gspl
from selenium.webdriver.support.ui import Select


class GoogleSearchPage(base_page.Page):
    @base_page.log_func_name
    def return_driver(self):
        return GoogleSearchPage(self.driver)

    @base_page.log_func_name
    def enter_search_string(self, search_string):
        logger = logging.getLogger(__name__)
        self.set_field_value(gspl.search_input_loc['search_input'], search_string)
        logger.info('%s string entered into search box', search_string)

    @base_page.log_func_name
    def click_search_element(self, element_type, element_name):
        logger = logging.getLogger(__name__)
        self.click_element(gspl.__dict__[element_type][element_name])
        logger.info('Element %s from %s clicked successfully', element_name, element_type)

    @base_page.log_func_name
    def press_enter_key(self, element_type, element_name, text_string):
        logger = logging.getLogger(__name__)
        self.set_field_value1(gspl.__dict__[element_type][element_name], text_string)
        logger.info('%s string entered into text box', text_string)

    @base_page.log_func_name
    def get_element_text(self, element_type, element_name):
        element = self.find_element(gspl.__dict__[element_type][element_name])
        element_text = element.text
        return element_text

    @base_page.log_func_name
    def select_from_list_box(self, element_type, element_name, text):
        element = self.find_element(gspl.__dict__[element_type][element_name])
        select = Select(element)
        select.select_by_visible_text(text)

    @base_page.log_func_name
    def press_down_arrow_key(self, element_type, element_name, text_string):
        logger = logging.getLogger(__name__)
        self.set_field_value1(gspl.__dict__[element_type][element_name], text_string)
        logger.info('%s string entered into text box', text_string)
