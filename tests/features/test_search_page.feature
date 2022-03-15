Feature: search in reserved website

    Scenario Outline: test search successfully
      Given open the page
      When we wrote haine "<haine>" in the search field

      Examples: Products
            | haine |
            | pijama |
            | tricou |
            | blugi |