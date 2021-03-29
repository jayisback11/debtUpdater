class CreateCustomer:
    def __init__(self):
        first_name = input('First Name: ')
        last_name = input('Last Name: ')
        debt_amount = input('Debt: ')

        file = open(f'./Customers/{last_name.title()}.{first_name.title()}.txt', 'w')

        file.write(f"Debt Amount: ${debt_amount}")
        file.write("\n\n")
        file.write("=====LOG UPDATES=====")

        file.close()