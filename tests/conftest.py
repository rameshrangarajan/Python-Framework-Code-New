import pytest
import os
import logging
import utils.utils as utils
from selenium import webdriver
from src.pages import login_page as login
from src.pages import search_page as search
from src.pages import google_search_page as google_search
from utils.email_pytest_report import email_pytest_report
from src.pages import goibibo_page as goibibo_search

def pytest_addoption(parser):
    """get parameters from command line using fixture function
    Args:
        parser (TYPE): Description
    """

    parser.addoption("--config", action="store", nargs='?',
                     type=str, default='config.qa_config',
                     help='the server configuration user would like to use')

    parser.addoption("--istestserver", action="store",
                     help='Specify a base url')

    parser.addoption("--username", action="store",
                     help='Specify a username if server is not test server')

    parser.addoption("--password", action="store",
                     help='Specify password if server is not test server')

    parser.addoption("--base_url", action="store",
                     help='Specify a base url')

    parser.addoption("--browser", action="store",
                     help='Specify browsers to run tests with')

    parser.addoption("--timeout", action="store",
                     help='Specify time to wait for conditions to be satisfied in browser')

    parser.addoption("--enable_automation_email_alert",
                     dest="enable_automation_email_alert",
                     help="Enable automation results email alert: Y or N",
                     default="N")

    parser.addoption("--sender_addr",
                     help="Specify email sender's address ")

    parser.addoption("--receiver_addrs",
                     help="Specify receivers names in comma separated format")

    parser.addoption("--email_server",
                     help="Specify email SMTP server")

@pytest.fixture
def enable_automation_email_alert(request):
    """ Return the value for enable_automation_email_alert
    """
    _enable_automation_email_alert = request.config.getoption("--enable_automation_email_alert")
    if not _enable_automation_email_alert:
        _enable_automation_email_alert = utils.get_config_var('ENABLE_AUTOMATION_EMAIL_ALERT',utils.process_config_file(request))
    return _enable_automation_email_alert


@pytest.fixture
def sender_addr(request):
    _sender_addr = request.config.getoption("--sender_addr")
    if not _sender_addr:
        _sender_addr= utils.get_config_var('SENDER_ADDR', utils.process_config_file(request))
    return _sender_addr

@pytest.fixture
def receiver_addrs(request):
    _receiver_addrs = request.config.getoption("--receiver_addrs")
    if not _receiver_addrs:
        _receiver_addrs = utils.get_config_var('RECEIVER_ADDRS', utils.process_config_file(request))
    return _receiver_addrs

@pytest.fixture
def email_server(request):
    _email_server = request.config.getoption("--email_server")
    if not _email_server:
        _email_server = utils.get_config_var('EMAIL_SERVER', utils.process_config_file(request))
    return _email_server


@pytest.fixture
def conf_username(request):
    """Return a valid user name
    """
    _user_name = request.config.getoption("--username")
    if not _user_name:
        _user_name = utils.get_config_var('USERNAME',
                                          utils.process_config_file(request))
    return _user_name


@pytest.fixture
def conf_password(request):
    """Return a valid password for user
    """
    pass_word = request.config.getoption("--password")
    if not pass_word:
        pass_word = utils.get_config_var('PASSWORD', utils.process_config_file(request))
    return pass_word

@pytest.fixture
def conf_is_test_server(request):
    """Set fixture of browser_type
    """
    _is_test_server = request.config.getoption("--istestserver")
    if not _is_test_server:
        _is_test_server = utils.get_config_var('IS_TEST_SERVER', utils.process_config_file(request))
    return _is_test_server

@pytest.fixture
def conf_base_url(request):
    """Set fixture of BASE_URL
    """
    _base_url = request.config.getoption("--base_url")
    if not _base_url:
        _base_url = utils.get_config_var('BASE_URL', utils.process_config_file(request))
    return _base_url


@pytest.fixture
def timeout(request):
    """Set fixture of timeout
    """
    _timeout = request.config.getoption("--timeout")
    if not _timeout:
        _timeout = utils.get_config_var('TIMEOUT', utils.process_config_file(request))
    return _timeout


@pytest.fixture
def browser_type(request):
    """Set fixture of browser_type
    """
    _browser = request.config.getoption("--browser")
    if not _browser:
        _browser = utils.get_config_var('BROWSER', utils.process_config_file(request))
    return _browser


@pytest.fixture
def app_login(driver, conf_is_test_server, conf_username, conf_password, conf_base_url ):
    """return the page handle upon login
    Args:
        driver (object): browser defined in conftest fixture
        username (str): username
        password (str): password
        base_url (str): base_url to launch
    """
    # if conf_is_test_server.lower() == 'yes':
    #
    #     search_page = search.SearchPage(driver)
    #     search_page.open(conf_base_url)
    #     print("Current URL is -: " + conf_base_url)
    #     return search_page.return_driver()
    # else:
    login_page = login.LoginPage(driver)
    login_page.open(conf_base_url)
    print("Current URL is -: " + conf_base_url)
    return login_page.login_user(conf_username, conf_password)


@pytest.fixture
def launch_browser(driver, conf_base_url):
    # returns the home page handle

    google_search_page = google_search.GoogleSearchPage(driver)
    google_search_page.open(conf_base_url)
    print("Current URL is -: " + conf_base_url)
    return google_search_page.return_driver()


@pytest.fixture
def launch_goibibo_in_browser(driver, conf_base_url):
    # returns the home page handle

    goibibo_page = goibibo_search.GoibiboPage(driver)
    goibibo_page.open(conf_base_url)
    print("Current URL is -: " + conf_base_url)
    return goibibo_page.return_driver()


@pytest.fixture
def dashboard_login(driver, conf_is_test_server, conf_username, conf_password, conf_base_url ):
    """return the page handle upon login
    Args:
        driver (object): browser defined in conftest fixture
        username (str): username
        password (str): password
        base_url (str): base_url to launch
    """
    if conf_is_test_server.lower() == 'yes':

        search_page = search.SearchPage(driver)
        search_page.open(conf_base_url + 'dashboard')
        return search_page.return_driver()
    else:
        login_page = login.LoginPage(driver)
        login_page.open(conf_base_url + 'dashboard')
        return login_page.login_user(conf_username, conf_password)

@pytest.yield_fixture
def driver(browser_type):
    """return a webdriver instance for testing
    """
    from sys import platform as _platform
    import os
    logger = logging.getLogger(__name__)
    prj_base_path = os.path.abspath('')
    driver_path = None

    if browser_type.lower() == 'chrome':
        from selenium.webdriver.chrome.options import Options

        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        # chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--ignore-ssl-errors=yes')
        chrome_options.add_argument('--ignore-certificate-errors')
        driver_path = prj_base_path + '/drivers/chromedriver/chromedriver_88'
        _driver = webdriver.Chrome(executable_path=driver_path, chrome_options=chrome_options)

    if browser_type.lower() == 'firefox':
        from selenium.webdriver.firefox.options import Options

        options = Options()
        #options.headless = True
        profile = webdriver.FirefoxProfile()
        profile.accept_untrusted_certs = True

        if _platform == "linux" or _platform == "linux2":
            driver_path = prj_base_path + '/drivers/geckodriver-linux32/geckodriver'
        elif _platform == "win32" or _platform == '"win64"':
            driver_path = r'C:\Users\rangarajan_r\Downloads\geckodriver-v0.26.0-win64\geckodriver.exe'
        _driver = webdriver.Firefox(executable_path=driver_path, options=options,firefox_profile=profile)

    if browser_type.lower == 'ie':
        if _platform == "linux" or _platform == "linux2":
            logger.error("IE browser is not supported on %s platform", _platform)
        elif _platform == "win32":
            driver_path = prj_base_path + '/drivers/IEDriverServer_Win32/IEDriverServer.exe'
        elif _platform == "win64":
            driver_path = prj_base_path + '/drivers/IEDriverServer_x64/IEDriverServer.exe'
        _driver = webdriver.Ie(executable_path=driver_path)

    _driver.maximize_window()
    yield _driver
    _driver.quit()


def pytest_terminal_summary(terminalreporter, exitstatus):
    "add additional section in terminal summary reporting."
    report_name = terminalreporter.config.getoption('--html')
    print(report_name)
    _enable_automation_email_alert = terminalreporter.config.getoption("--enable_automation_email_alert")
    if not _enable_automation_email_alert:
        _enable_automation_email_alert = utils.get_config_var_from_server_config('ENABLE_AUTOMATION_EMAIL_ALERT')
        print("enable_automation_email_alert option is set to false. Please add --enable_automation_email_alert=true or make it false in server.config file.")

    if _enable_automation_email_alert.lower() == 'true':
        _email_server=utils.get_config_var_from_server_config('EMAIL_SERVER')
        _receiver_addrs=', '.join(utils.get_config_var_from_server_config('RECEIVER_ADDRS'))
        _sender_addr=utils.get_config_var_from_server_config('SENDER_ADDR')
        if not report_name:
            print("html report won't be generated as --html option is not used. Please use --html=report.html")
        else:
            email_pytest_report.send_test_report_email(_email_server,_receiver_addrs, _sender_addr,report_file_path=report_name)
