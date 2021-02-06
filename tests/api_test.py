from datetime import datetime
from csv import writer
from csv import reader
import requests
import pytest
import csv
import json
from hamcrest import *
from src.pages import createUsers

from pytest_bdd import (
    given,
    scenarios,
    then,
    when,
    parsers
)

scenarios('../feature_files/api_test.feature')


class global_variables(object):
    def __init__(self):
        self.url = None
        self.response = None
        self.response_time = 0
        self.response_sum = 0
        self.f = None
        self.response_time_list = []


gl_var = global_variables()


@given(parsers.cfparse('user sets API server for {search} end point'))
def set_url(conf_base_url, search):
    gl_var.url = conf_base_url + search


@when('user does the post call with search string as <search_string_list>')
def execute_search_post_call(search_string_list):
    search_strings = search_string_list.split(',')
    gl_var.response_time_list.append(str(datetime.now()))
    for string in search_strings:
        post_fields = {"query": string, "page_number": 1, "query_type": "search", "time_filter": "all"}
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'session'
                             '=.eJyrVkrNTczMUbJSCkrMTS3O0AtKzEtPLErMSsxziMgvykzMK9Fzzs9V0lHKA8rDlSkglAGlSvMyC0tT4zNTgPJFcIn4IqVaADHPIVM'}
        gl_var.response = requests.post(gl_var.url, data=post_fields, headers=headers, verify=False)
        gl_var.response_time = gl_var.response.elapsed.total_seconds()
        gl_var.response_time_list.append(str(gl_var.response_time))
        print(gl_var.response_time)
        gl_var.response_sum = gl_var.response_sum + gl_var.response_time
    gl_var.response_time_list.append(str(gl_var.response_sum / 10))
    print("Average response time for search query -: " + str(gl_var.response_sum / 10))


@then('write response time in a file')
def write_response_time():
    gl_var.f = open("KMP_Response_Time.txt", "a")
    i = 0
    for item in gl_var.response_time_list:
        if i == 0:
            gl_var.f.write(item + " : ")
        elif i == 11:
            gl_var.f.write("Average Time : " + item)
        else:
            gl_var.f.write(item + " , ")

        i = i + 1
    gl_var.f.write('\n')


@given('user sets API url with <pagenumber>')
def set_url_for_get(conf_base_url, pagenumber):
    gl_var.url = conf_base_url + pagenumber


@when('user does the get call')
def execute_search_get_call():
    headers = {
        'Content-Type': 'application/json',
        'Cookie': '__cfduid=de08e8942fd265f45c530208fb65774991612513043'
    }
    payload = {}
    # gl_var.response = requests.request("GET", gl_var.url, headers=headers, data=payload)
    gl_var.response = requests.get(gl_var.url, headers=headers, data=payload)
    gl_var.response_time = gl_var.response.elapsed.total_seconds()


@then('print the response text and the response time for get')
def print_response_details():
    pretty_json = json.loads(gl_var.response.text)
    print(json.dumps(pretty_json, indent=2))
    print(gl_var.response_time)
    print(gl_var.response.status_code)
    assert_that(gl_var.response.status_code, equal_to(200))
    assert_that(gl_var.response.text, contains_string("Michael"))
    assert gl_var.response.status_code == 200


@given('user sets API url for post')
@pytest.fixture()
def set_url_for_post(conf_base_url):
    gl_var.url = conf_base_url


@when('user does the post call with payload as <name> and <job>')
def execute_search_for_post(name, job):
    print('Inside post request method')
    headers = {
        'Content-Type': 'application/json',
        'Cookie': '__cfduid=de08e8942fd265f45c530208fb65774991612513043'
    }
    # payload = createUsers.CreateUsers(name, job)
    payload = "{\r\n    \"name\":" + name + ",\r\n    \"job\":" + job + "\r\n}"
    # payload = dict({"name": name, "job": job})

    # gl_var.response = requests.request("GET", gl_var.url, headers=headers, data=payload_string)
    gl_var.response = requests.post(gl_var.url, data=payload, headers=headers, verify=False)
    # gl_var.response = requests.request("POST", gl_var.url, headers=headers, data=payload)
    gl_var.response_time = gl_var.response.elapsed.total_seconds()


@then('print the response text and the response time for post')
def print_response_details_1():
    pretty_json = json.loads(gl_var.response.text)
    print(json.dumps(pretty_json, indent=2))
    print(gl_var.response_time)
    print(gl_var.response.status_code)
    assert_that(gl_var.response.status_code, equal_to(201))
    assert_that(gl_var.response.text, contains_string("Ramesh"))
    assert gl_var.response.status_code == 201
