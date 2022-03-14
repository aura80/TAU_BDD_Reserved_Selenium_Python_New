Feature: search in reserved website

    Scenario: test search successfully
      Given open the page
      When we wrote pijama "<pijama>" in the search field

      Examples: Products
            | pijama |
            | pijama |