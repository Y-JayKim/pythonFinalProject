# manage_account.py
#
#
#
# Yeonjae Kim   A00967079   2A
#
from chequing import Chequing
from saving import Saving
from term_saving import TermSaving


def main():

    chequing1 = Chequing("Sally", 1000)
    chequing1.withdraw(50)
    print(chequing1.balance)
    chequing1.withdraw(850)
    chequing1.withdraw(500)
    chequing1.post_cheque(1000)
    chequing1.deposit(2000)
    chequing1.interest()

    saving1 = Saving("Joe", 5000)
    saving1.deposit(100)
    print(saving1.balance)
    saving1.withdraw(500)
    saving1.deposit(2000)
    saving1.interest()
    saving1.change_name("Joseph")

    # $6000 is already in the log because of the withdraw minimum date allowance reason
    # Because of the date problem, negative balance problem occurs
    term_saving1 = TermSaving("Sally", 1000)
    term_saving1.withdraw(5500)  # possible because $6000 has deposited 1 year before
    term_saving1.withdraw(1000)  # Impossible because only $500 deposited more than 60 days before
    term_saving1.deposit(2000)
    term_saving1.interest()

    print(chequing1)
    print(saving1)
    print(term_saving1)

    print("\n\nChequing Account\n")
    for nam, amo, day in chequing1.get_transaction:
        print("%-15s $%-15s @%-15s" % (nam, amo, day))
    print("\n\nSaving Account\n")
    for nam, amo, day in saving1.get_transaction:
        print("%-15s $%-15s @%-15s" % (nam, amo, day))
    print("\n\nTerm Saving Account\n")
    for nam, amo, day in term_saving1.get_transaction:
        print("%-15s $%-15s @%-15s" % (nam, amo, day))


if __name__ == "__main__":
    main()








