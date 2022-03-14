Feature: register on reserved website

    Scenario: test register unsuccessfully
        Given open the register page
        When adding email "<email>"
        And adding firstname "<firstname>"
        And adding lastname "<lastname>"
        And adding password "<password>"
        And the user click Create Account button
        Then "<error>" error message is displayed

        Examples: Amounts
            |  email             | firstname | lastname | password | error           |
            | testing            |    ana    |  ionescu | Start123 | Vă rugăm să introduceți numai caractere valide |
            | testing@yahoo.com  |   ioana   |    " "   | Start123 | Vă rugăm să introduceți numai caractere valide |
            | testing1@yahoo.com |   dana    |  ionescu | Star3    | Min 6 caractere |