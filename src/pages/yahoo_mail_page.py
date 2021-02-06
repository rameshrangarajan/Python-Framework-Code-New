import logging
from src.pages import base_page
from src.locators.yahoopage_locators import YahooPageLocators as ypl
from selenium.webdriver.common.action_chains import ActionChains


class YahooMailPage(base_page.Page):
    @base_page.log_func_name
    def return_driver(self):
        return YahooMailPage(self.driver)

    @base_page.log_func_name
    def click_mail_button(self, element_type, element_name):
        logger = logging.getLogger(__name__)
        self.click_element(ypl.__dict__[element_type][element_name])
        logger.info('Element %s from %s clicked successfully', element_name, element_type)

    @base_page.log_func_name
    def get_element_text(self, element_type, element_name):
        element = self.find_element(ypl.__dict__[element_type][element_name])
        element_text = element.text
        return element_text

    @base_page.log_func_name
    def hover_over(self, element_type, element_name):
        self.hover_over_element(ypl.__dict__[element_type][element_name])

    @base_page.log_func_name
    def click_signout_link(self, element_type, element_name):
        logger = logging.getLogger(__name__)
        self.click_element(ypl.__dict__[element_type][element_name])
        logger.info('Element %s from %s clicked successfully', element_name, element_type)
