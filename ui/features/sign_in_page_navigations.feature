@sanity
Feature: Sign In Page Navigation

    @allure.link.TestCaseLink:TZ-1234
  Scenario: Navigate from Login screen to Create account screen
    Given I Verify Login account screen page displayed
    When And I Click on Signup to redirect create account page
    Then Verify Create account screen page displayed

  @allure.link.TestCaseLink:TZ-1234
  Scenario: Create Account with auto generated data
      Given I Verify Login account screen page displayed
      When And I Click on Signup to redirect create account page
      Then Verify Create account screen page displayed
      And  Enter First Name
      Then Enter Last Name
      And Select Country
      Then I click on continue button
      And I entering email in email field
      Then I entering password in password field
      And I Click on next button on register page
      Then I Click on Register button

  @allure.link.TestCaseLink:TZ-1234
  Scenario: Verify Email field error message displayed while login without entering email
      Given I Verify Login account screen page displayed
      When I Click on Login button
      Then I verify for email error field msg
