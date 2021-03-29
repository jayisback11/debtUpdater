import os
from datetime import date
import re


class UpdateCustomer:
    def __init__(self):
        for root, dirs, files in os.walk("./Customers"):
            index = 1
            self.list_of_customers = {}
            for filename in files:
                self.list_of_customers[index-1] = filename
                names = str(filename).split('.')
                print(f"{index}.) {names[1].title()} {names[0].title()}")
                index += 1

    def update_debt(self, choice):
        file = open(f"./Customers/{self.list_of_customers[choice-1]}", 'r+')

        first_line = file.readline()
        dollar_sign_index = int(first_line.find('$'))
        dollar_debt = int(first_line[(dollar_sign_index+1):])
        print(f"Current Debt: ${dollar_debt}")

        print("1. Update Debt")
        print("3. Exit")
        choices = int(input("Select an option: "))

        if choices == 1:
            amount = int(input("Enter amount: "))
            new_debt = dollar_debt + amount

            with open(f"./Customers/{self.list_of_customers[choice-1]}", "r+") as f:
                data = f.read()
                f.seek(0)
                f.write(re.sub(f"{dollar_debt}", f"{new_debt}", data))
                f.truncate()

            today = date.today()
            current_date = today.strftime("%b-%d-%Y")

            with open(f"./Customers/{self.list_of_customers[choice-1]}", 'a') as f2:
                if amount > 0:
                    f2.writelines(f'\n* +{amount} at {current_date}')
                    print("UPDATED SUCCESSFULLY!")
                else:
                    f2.writelines(f'\n* {amount} at {current_date}')
                    print("UPDATED SUCCESSFULLY!")







