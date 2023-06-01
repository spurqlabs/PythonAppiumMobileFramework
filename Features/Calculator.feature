@iOS
#android
Feature: Simple Calculator
  Addition of two numbers

  Scenario: Verify addition of two numbers
    Given I am on calculator home page
    When I enter '4'
    And I enter operator of addition
    And Enter number '2'
    And I enter operator '='
    Then I see result as '6'

