# ======================================================
# 1. FARM MODEL (OOP + Inheritance)
# ======================================================

class Animal:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name, "is eating")

    def sleep(self):
        print(self.name, "is sleeping")

    def speak(self):
        print(self.name, "makes a sound")


class Cow(Animal):

    def speak(self):
        print(self.name, "says Moo!")

    def produce_milk(self):
        print(self.name, "is producing milk")


class Chicken(Animal):

    def speak(self):
        print(self.name, "says Cluck!")

    def lay_eggs(self):
        print(self.name, "laid an egg")


class Sheep(Animal):

    def speak(self):
        print(self.name, "says Baa!")

    def grow_wool(self):
        print(self.name, "is growing wool")


def farm_demo():

    print("\n=== FARM DEMO ===")

    cow = Cow("Bessie", 4)
    chicken = Chicken("Chicko", 2)
    sheep = Sheep("Dolly", 3)

    animals = [cow, chicken, sheep]

    for a in animals:
        print("\nAnimal:", a.name, "Age:", a.age)
        a.eat()
        a.sleep()
        a.speak()

    cow.produce_milk()
    chicken.lay_eggs()
    sheep.grow_wool()



# ======================================================
# 2. BANK APPLICATION
# ======================================================

class Account:

    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def __str__(self):
        return f"{self.account_number}, {self.name}, {self.balance}"


class Bank:

    FILE = "accounts.txt"

    def __init__(self):
        self.accounts = {}
        self.load_from_file()


    # Create account
    def create_account(self):

        name = input("Enter name: ")
        deposit = float(input("Initial deposit: "))

        account_number = str(len(self.accounts)+1001)

        acc = Account(account_number,name,deposit)

        self.accounts[account_number] = acc

        self.save_to_file()

        print("Account created:", account_number)


    # View account
    def view_account(self):

        num = input("Account number: ")

        if num in self.accounts:
            print(self.accounts[num])
        else:
            print("Account not found")


    # Deposit
    def deposit(self):

        num=input("Account number: ")

        if num not in self.accounts:
            print("Account not found")
            return

        amount=float(input("Amount: "))

        if amount<=0:
            print("Invalid amount")
            return

        self.accounts[num].balance+=amount

        self.save_to_file()

        print("Deposited")


    # Withdraw
    def withdraw(self):

        num=input("Account number:")

        if num not in self.accounts:
            print("Account not found")
            return

        amount=float(input("Amount: "))

        if amount>self.accounts[num].balance:
            print("Insufficient balance")
            return

        self.accounts[num].balance-=amount

        self.save_to_file()

        print("Withdraw successful")


    # Save file
    def save_to_file(self):

        with open(self.FILE,"w") as f:

            for acc in self.accounts.values():

                f.write(str(acc)+"\n")


    # Load file
    def load_from_file(self):

        try:
            with open(self.FILE) as f:

                for line in f:

                    num,name,balance=line.strip().split(",")

                    self.accounts[num.strip()] = Account(
                        num.strip(),
                        name.strip(),
                        float(balance)
                    )
        except:
            pass



    def menu(self):

        while True:

            print("\n=== BANK APP ===")

            print("1 Create Account")
            print("2 View Account")
            print("3 Deposit")
            print("4 Withdraw")
            print("5 Exit")

            ch=input("Choice: ")

            if ch=="1":
                self.create_account()

            elif ch=="2":
                self.view_account()

            elif ch=="3":
                self.deposit()

            elif ch=="4":
                self.withdraw()

            elif ch=="5":
                break



# ======================================================
# MAIN MENU
# ======================================================

print("\nSelect Program")

print("1 Farm Model")
print("2 Bank Application")

choice=input("Choice: ")


if choice=="1":
    farm_demo()

elif choice=="2":
    Bank().menu()

else:
    print("Exit")