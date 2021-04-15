from Bank import Bank
from Client import Client

bank = Bank()
print("Welcome to the {}".format(bank.Name))


def Choose(choice1, choice2, choice3, *args):
    print()
    print("Select an option.")
    print("1. {}".format(choice1))
    print("2. {}".format(choice2))
    print("3. {}".format(choice3))
    if args:
        print("4. {}".format(args[0]))

    if args:
        choices = [choice1, choice2, choice3, args[0]]
    else:
        choices = [choice1, choice2, choice3]
    global option
    option = input("Enter your choice : ")
    if option not in choices:
        print()
        print("Invalid option")
        print("Please choose again!")
        Choose(choice1, choice2, choice3, *args)


running = True
while running:
    Choose("New Account", "Existing Account", "Exit")
    if option == "New Account":
        Name = input("Name: ")
        current_client = Client(Name)
        bank.update_db(current_client)
        amount = int(input("Amount you want to deposit : "))
        current_client.deposit(amount)
    elif option == "Existing Account":
        Name = input("Name: ")
        account_no = int(input("Account No. : "))
        current_client = bank.authentication(Name, account_no)
        if current_client:
            print()
            print("Authentication succesfull")
            print("Welcome {}!".format(current_client.name))

            open = True
            while open:
                Choose("Deposit", "Withdraw", "Display Balance", "Exit")
                if option == "Deposit":
                    amount = int(input("Deposit Amount: "))
                    current_client.deposit(amount)
                elif option == "Withdraw":
                    amount = int(input("Withdraw Amount: "))
                    current_client.withdraw(amount)
                elif option == "Display Balance":
                    current_client.display_balance()
                elif option == "Exit":
                    print()
                    print("Thank you")
                    print("Please come again!!")
                    open = False

        else:
            print()
            print("Authentication Failed!!")
            print("No match found.")
    elif option == "Exit":
        print()
        print("Thank you")
        print("Please come again!!")
        running = False
