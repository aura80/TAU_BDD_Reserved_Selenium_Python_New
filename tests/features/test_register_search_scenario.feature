Feature: search in reserved website

    Scenario Outline: test search successfully
      Given open the page
      When we wrote haine "<haine>" in the search field

      Examples: Products
            | haine |
            | pijama |
            | tricou |
            | blugi |

    Scenario Outline: check search functionality
      Given open the search page
      When the user types "<item>" in the search bar
      Then each result contains "<item>" in name

      Examples: Searched item
            | item|
            | pijama |
            | rochie |
            | bluza |

    Scenario: test automated register on reserved website successfully
      Given open the register page
      When generate random email
      When generate random firstname lastname password
      When searching element fuste
      When searching element assert
      When searching element pijama
