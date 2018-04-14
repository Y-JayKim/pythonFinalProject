# pythonFinalProject

GUI Description
1. Starts from the "controller.py" by logging in.  The user has to type his/her SIN number and their PIN number as a password. There is a login option
   with QR code but currently it's not functioning.
    - If the user types wrong SIN or PIN, a messagebox pops up.
    - If the user wants to register or lost one's SIN/PIN, he/she has to contact with the bank teller for security. If the user clicks those texts, a
      messagebox pops up saying he/she has to go to a bank.

2. After successfully logging in, there are six actions that user can use. Those are 'Deposit', 'Withdraw', 'Check Balance', 'Transfer', 'Show Account
   Information' and 'Help.'
    - If the user clicks 'deposit/withdraw/transfer', it will show the types of accounts that user has. Then, user can choose account that they want to
      perform certain action. After choosing an account, the user will see the window that one can type amount. For deposit, there is no limit but wit-
      hdraw and transfer have limits that the user's input should not exceed their account balance.
      If the user performs any action, it will remain in the transaction log. ex)"You {action type} ${amount} on{date}."
    - If the user clicks 'Check Balance', it will show the balance of account depends on what accounts that the user have.