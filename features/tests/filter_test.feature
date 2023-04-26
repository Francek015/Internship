# Created by sfrog at 2023-04-22
Feature: Filter testing

  Scenario: User can search then filter results
    Given Open cureskin results for cure
    When verify 18 results found for “cure”
    When click sort by
    When click high to low
    Then Verify order



