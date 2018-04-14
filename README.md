# pythonFinalProject

GUI Description

1. Starts from the "controller.py" by logging in.  The user has to type his/her SIN number and their PIN number as a password. There is a login option
   with QR code but currently it's not functioning.
    - If the user types wrong SIN or PIN, a messagebox pops up.
    - If the user wants to register or lost one's SIN/PIN, he/she has to contact with the bank teller for security. If the user clicks those texts, a
      messagebox pops up saying he/she has to go to a bank.

2. After successfully logging in, there are six actions that user can use. Those are 'Deposit', 'Withdraw', 'Check Balance', 'Transfer', 'Account
   History' and 'Help.'
    - If the user clicks 'deposit/withdraw/transfer', it will show the types of accounts that user has. Then, user can choose account that they want to
      perform certain action. After choosing an account, the user will see the window that one can type amount. For deposit, there is no limit but wit-
      hdraw and transfer have limits that the user's input should not exceed their account balance. After that, user's action will be recorded in the
      transaction log. ex)"You {action type} ${amount} on{date}."

    - If the user clicks 'Check Balance', it will show the balance of account depends on what accounts that the user have.

    - If the user clicks 'Transfer', it will show accounts that the user has and he/she can choose the account where they want to transfer from.
      Then, it will show the page where user can type both amount and destination account. If the user types the amount exceeding the balance of the
      account or wrong destination, the messagebox pops up saying "Invalid Input." If the user typed right inputs, the messagebox pops up saying "You
      transfered ${amount} to {destination account}."

    - If the user clicks 'Account History', the user can choose account to view the history. Then, a window with a listbox containing the transaction
      logs pops up.

    - If the user clicks 'Help', the user can see the bank number where they can get help when necessity.

3. **When the user is typing the amount, he/she has to use the keypad.

4. Each Back button on top-left corner allows users to go back to main page where they can choose action.


//-----------------------------------------------------------------------------------------------------------------------------------//

CLI Instruction

1. username and password for Signing in as Administrator is in the File 'manager_account.csv'

2. You can choose the action what you want to do for the client (add an Account, delete an account, Transaction report, change PIN)

3. SIN must be 9 digit number like real-world

4. Account selection need to be 'chequing' or 'saving' or 'term saving'

5. One SIN can have only one type of account. Therefore maximum account that one SIN can hold is 3 (saving, chequing, term saving)

6. Once the system creates an account, it creates 1000x_log.txt (1000x is the account number), and the username and password for GUI
The default password for all PIN is 123
