#
#
#
#
#
#


class ManageSelection:
    def __init__(self):
        self.selection = ''
        print("Please select an option\n\n")

    def selection_page(self):
        print("1.Create an User Account    | 2.Delete existing User Account \n3.User's Transaction Report | "
              + "4. Change PIN\n5. Show options again       | 0.Exit \n\n")
        self.selection = input("Please Enter a Number above: ")

    def not_in_option(self):
        print("\nInvalid Input. Please try again.\n")
        print("Enter 6 to see the menu again\n")
        self.selection = input("Please Enter a Number: ")