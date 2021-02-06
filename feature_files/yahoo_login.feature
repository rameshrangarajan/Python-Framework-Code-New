@yahoo_login @regression @training
Feature: Test cases for Yahoo login scenarios

@tc_yahoo_login-1
Scenario Outline: Log into yahoo and verify that user is logged in
    Given the user logs into the application
    When the user clicks the Mail button
    Then the login name label is Ramesh

@tc_yahoo_login-2
Scenario Outline: Log into yahoo and then log out and verify that user has logged out
    Given the user logs into the application
    And the user clicks the Mail button
    When the user clicks on the Sign Out link
    Then the sign in label is Sign in