import logging
from src.pages import base_page
from src.locators.dashboardPage_locators import DashboardPageLocators as dpl


class DashboardPage(base_page.Page):
    @base_page.log_func_name
    def return_driver(self):
        return DashboardPage(self.driver)


    @base_page.log_func_name
    def get_element_text(self,element_type, element_name):
        element = self.find_element(dpl.__dict__[element_type][element_name])
        element_text = element.text
        return element_text

    @base_page.log_func_name
    def is_element_displayed_and_enabled(self, element_type, element_name):
        return self.find_element(dpl.__dict__[element_type][element_name]).get_attribute("src")



    @base_page.log_func_name
    def find_all_elements(self, element_type, element_name):
        return self.find_elements(dpl.__dict__[element_type][element_name])

    @base_page.log_func_name
    def findelement(self, element_type, element_name, timeout=None):
        try:
            return self.find_element(dpl.__dict__[element_type][element_name], timeout)
        except:
            return False
