import random

class Client:

    def __init__(self, name):
        self.account = {}
        self.name = name
        self.account["Name"] = name
        self.account_no = random.randint(100000, 999999)
        self.account["Account_No"] = self.account_no
        self.account["Balance"] = 0
        self.passbook = {}
        print("Your account has been created succesfully.")
        print("Your account no. is {}".format(self.account_no))

    def deposit(self, amount):
        self.account["Balance"] += amount
        print("{} has been credited to your account.".format(amount))

    def withdraw(self, amount):
        if amount >= self.account["Balance"]:
            print("Not enough Funds!!")
        else:
            self.account["Balance"] -= amount
            print("{} has been debited from your account".format(amount))

    def display_balance(self):
        print("Balance : {}".format(self.account["Balance"]))
