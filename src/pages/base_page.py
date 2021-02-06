"""
This page is used to provide common functionality across all application pages
This page have override methods for finding elements, clicking buttons, entering text, etc.
"""
from selenium.webdriver.common.action_chains import ActionChains
from functools import wraps
import logging
from selenium.common.exceptions import (
    ElementNotVisibleException,
    StaleElementReferenceException,
    WebDriverException,
    NoSuchElementException,
    TimeoutException
)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys


def log_func_name(func):
    @wraps(func)
    def tmp(*args, **kwargs):
        logger = logging.getLogger(func.__module__)
        logger.info("Calling %s ..." % func.__name__)
        return func(*args, **kwargs)
    return tmp


class Page(object):
    """
        Base class. This will be inherited by all page classes
    """
    def __init__(self, selenium_driver, timeout=60):
        """
            Args:
            selenium_driver (object): selenium webdriver to navigate pages with
            timeout (int, optional): seconds to wait
        """
        self.driver = selenium_driver
        self.timeout = timeout

    @log_func_name
    def open(self, url):
        """open the url using webdriver's get function.
        Args:
            url (str): url to access the project
        """
        logger = logging.getLogger(__name__)
        logger.info("Opening page with url %s", url)
        self.driver.get(url)
        return self.driver

    @log_func_name
    def find_element(self, locator, timeout=None):
        """Return the element specified with locator
        Args:
            locator (str): used to evaluate presence of element
            timeout (int, optional): seconds to wait
        """
        if timeout is None:
            timeout = self.timeout

        element = None
        logger = logging.getLogger(__name__)

        try:
            logger.info("Finding element with %s locator", locator)
            element = WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located(locator))
        except:
            logger.exception("Element with %s locator not found!", locator)
        finally:
            return element

    @log_func_name
    def find_elements(self, locator, timeout=None):
        """Return the element specified with locator
        Args:
            locator (str): used to evaluate presence of element
            timeout (int, optional): seconds to wait
        """
        if timeout is None:
            timeout = self.timeout

        element = None
        logger = logging.getLogger(__name__)

        try:
            logger.info("Finding elements with %s locator", locator)
            elements = WebDriverWait(self.driver, timeout).until(ec.presence_of_all_elements_located(locator))
        except:
            logger.exception("Elements with %s locator not found!", locator)
        finally:
            return elements

    @log_func_name
    def click_element(self, locator, timeout=None):
        """Click the element specified with locator
        Args:
            locator (str): used to evaluate presence of element
            timeout (int, optional): seconds to wait
        """
        if timeout is None:
            timeout = self.timeout

        logger = logging.getLogger(__name__)
        logger_message = "Clicking on element with %s value for locator"
        logger.info(logger_message, locator)

        try:
            element_to_click = self.find_element(locator)
            element_to_click.click()
            logger.info("Element successfully clicked!")
        except (WebDriverException, ElementNotVisibleException, StaleElementReferenceException):
            self.scroll_to_make_element_visible_on_screen(locator)
            element_to_click = self.find_element(
                locator, timeout)
            element_to_click.click()
            logger.info("Element is enabled, displayed and clickable.")

    @log_func_name
    def set_field_value(self, locator, text, timeout=None):
        """Set field value in locator provided with text value supplied.
      Args:
            locator (str): used to evaluate presence of element
            text (str): text to set a field to
            timeout (int, optional): seconds to wait
        """
        if not timeout:
            timeout = self.timeout

        try:
            logger = logging.getLogger(__name__)
            logger_message = "Entering %s on element with %s value for locator"
            logger.info(logger_message, text, locator)
            input_element = WebDriverWait(self.driver, timeout).until(
                ec.element_to_be_clickable(locator))
            input_element.clear()
            input_element.send_keys(text)

        except:
            self.scroll_to_make_element_visible_on_screen(locator)
            input_element = self.find_element(locator)
            input_element.clear()
            input_element.send_keys(text)

    @log_func_name
    def set_field_value1(self, locator, text, timeout=None):
        """Set field value in locator provided with text value supplied.
      Args:
            locator (str): used to evaluate presence of element
            text (str): text to set a field to
            timeout (int, optional): seconds to wait
        """
        if not timeout:
            timeout = self.timeout

        try:
            logger = logging.getLogger(__name__)
            logger_message = "Entering %s on element with %s value for locator"
            logger.info(logger_message, text, locator)
            input_element = WebDriverWait(self.driver, timeout).until(
                ec.element_to_be_clickable(locator))
            # input_element.clear()
            input_element.send_keys(text)

        except:
            self.scroll_to_make_element_visible_on_screen(locator)
            input_element = self.find_element(locator)
            # input_element.clear()
            input_element.send_keys(text)

    @log_func_name
    def verify_element_is_displayed_and_enabled(self, locator, timeout=None):
        """ Verifies if element is displayed and enabled or not
        Args:
        locator(tuple): location of webelement to be checked
        """
        logger = logging.getLogger(__name__)
        logger_message = "waiting for element with %s as locator"
        logger.info(logger_message, locator)
        if not timeout:
            timeout = self.timeout
        try:
            elem = self.find_elements(locator, timeout)
            for element in elem:
                if element.is_displayed():
                    if element.is_enabled():
                        logger.info("Element is enabled")
                        return True
                else:
                    logger.info("Element is not enabled")
                    return False
        except Exception:
            return False

    @log_func_name
    def wait_for_element_to_be_present_and_clickable(self, locator, timeout=None):
        """ wait method for elements to be present and clickable """
        if timeout is None:
            timeout = self.timeout

        element = None
        try:
            logger = logging.getLogger(__name__)
            logger_message = "waiting for element with %s as locator"
            logger.info(logger_message, locator)

            element = WebDriverWait(self.driver, timeout).until(
                ec.element_to_be_clickable(locator)
            )
            logger.info("this element is: %s", element)
            return element

        except WebDriverException:
            logger_message = "Element with %s locator not found!"
            logger.exception(logger_message, locator)

    @log_func_name
    def scroll_to_make_element_visible_on_screen(self, locator_template):
        """
            Scroll page till the required element gets visible
        """
        elem_to_click = self.find_element(locator_template)
        elem_click_location = elem_to_click.location_once_scrolled_into_view
        wrapper_height = self.driver.execute_script("return document.querySelector('.page-head').offsetHeight")
        js_script_execute = "window.scrollTo({location[x]},{location[y]} - " \
                            "{wrapper_height});".format(location=elem_click_location, wrapper_height=wrapper_height)
        self.driver.execute_script(js_script_execute)

    @log_func_name
    def get_window_handle(self):

        oldtab = self.driver.current_window_handle
        return oldtab


    @log_func_name
    def switch_to_previous_tab(self,oldtab):

        self.driver.switch_to.window(oldtab)

    @log_func_name
    def hover_over_element(self, locator):
        element = self.find_element(locator)
        ActionChains(self.driver).move_to_element(element).perform()

