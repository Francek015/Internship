# Created by sfrog at 2023-04-26
Feature: Email address test

  Scenario: confirm user enters valid email
    Given Open cureskin shop page
    When close popup
    When enter invalid email hello
    When enter valid email beb@gmail.com
    Then verify that To continue, let us know you're not a robot.