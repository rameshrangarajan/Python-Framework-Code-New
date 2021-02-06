import csv
from importlib import import_module


def process_config_file(request):
    """Process and load valid configs from command line arg --config
    """
    user_config = None
    config_name = request.config.getoption('--config')
    try:
        user_config = import_module(config_name)
        return user_config
    except ImportError:
        error_msg = 'No config named {}. Make sure you are refering correct config file'.format(config_name)
        raise ImportError(error_msg)

    except AttributeError:
        err_msg = 'Specify a config to use or remove the config flag'
        raise ImportError(err_msg)


def get_config_var(var_name, config_module):
    """Get specified variable from config module
    Args:
        var_name (str): The name of the variable to access from the config module object.
    """
    try:
        return config_module.__dict__[var_name]
    except (AttributeError, KeyError):
        import config.base as cb
        try:
            return cb.__dict__[var_name]
        except:
            err_msg = "Couldn't find {} in base config module, " \
                      "are you sure that's the variable name?".format(var_name)
            raise ImproperlyConfigured(err_msg)


def get_config_var_from_server_config(var_name):
    """Get specified variable value from from server_config file.
       Args:
           var_name (str): The name of the variable to access from server_config file.
       """
    config_value = import_module('config.server_config')
    get_value= config_value.__dict__[var_name]
    return get_value


class ImproperlyConfigured(Exception):
    """Exceptions for unset environment variables
    """
    def __init__(self, value):
        Exception.__init__(self)
        self.value = value

    def __str__(self):
        return repr(self.value)


def retrieve_csv_data(filename):
    """
    Read csv file and process header and row data into python lists objects
    named headers and results.

    Args:
        filename (str): file name of csv data

    Returns:
        object: tuple of csv data in headers and rows
    """
    results = []
    headers = ()
    with open(filename, encoding='utf-8') as opened_file:
        csv_processed_file = csv.reader(opened_file)
        headers = next(csv_processed_file)

        results = [row for row in csv_processed_file]
    return headers, results

