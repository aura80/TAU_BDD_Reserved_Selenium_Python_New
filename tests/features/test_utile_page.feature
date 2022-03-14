Feature: automated register on reserved website

      Scenario: test register successfully
        Given open the register page
        When generate random email
        When generate random firstname lastname password
        When searching element fuste
        When searching element assert
        When searching element pijama
