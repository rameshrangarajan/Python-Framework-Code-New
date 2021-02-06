@training
Feature: Test cases for training scenarios

@tc_training-1
Scenario Outline: Verify that user is able to submit training grading
     Given the user logs into the application
     And the user enter adcolony into search text box
     And the user clicks on the search button
     And the user clicks on the grader handle
     When user clicks on the Submit button
     Then verify that the message You have successfully submitted your grading! appears

@tc_training-2
Scenario Outline: Verify that user is able to reset training grading
     Given the user logs into the application
     And the user enter adcolony into search text box
     And the user clicks on the search button
     And the user clicks on the grader handle
     When user clicks on the Reset button
     Then verify that the slider handle is at position Na
