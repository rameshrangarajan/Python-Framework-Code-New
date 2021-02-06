@api_test @regression
Feature: Test case for API testing

@tc_api
Scenario Outline: Measure average response time taken for search
     Given user sets API server for search end point
     When user does the post call with search string as <search_string_list>
     Then write response time in a file

     Examples:
    | search_string_list                                                                                        |
    | iot,xoriant,girish gaitonde,NLP capabilities,Accenture,Azure,Microsoft,CNN,Robotic process automation,aws |


@tc_api_test-2
Scenario Outline: Sample GET request automation
     Given user sets API url with <pagenumber>
     When user does the get call
     Then print the response text and the response time for get

     Examples:
     | pagenumber |
     | ?page=2    |


@tc_api_test-3
Scenario Outline: Sample POST request automation
     Given user sets API url for post
     When user does the post call with payload as <name> and <job>
     Then print the response text and the response time for post

     Examples:
     | name       | job                 |                                                   |
     | "Ramesh"   | "QA Professional"   |