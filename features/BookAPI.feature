# Created by 91995 at 02-07-2021
Feature: Validation of books addition and deletion
  # Enter feature description here

  Scenario: Validate add book through API
    Given the book details which needs to be added to Library
    When we execute the AddBook PostAPI method
    Then book successfully added

