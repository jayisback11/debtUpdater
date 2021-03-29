import createCustomer
import updateCustomer
import os


while True:
    print("========MAIN MENU=========")
    print("1. Create Customer")
    print("2. Update Customer")
    print("==========================")
    print("Select one, e.g. 1:")

    try:
        choice = int(input("> "))
    except ValueError:
        print("Invalid input. Please type '1' to create a customer or '2' to update a customer.")
        choice = 3
        continue

    if choice == 1:
        createCustomer.CreateCustomer()
    elif choice == 2:
        update = updateCustomer.UpdateCustomer()
        if len(update.list_of_customers) == 0:
            print("No Customers")
            continue
        print("==================")
        print("List of Customers")
        customer_choice = int(input("Select a Customer: "))
        update.update_debt(customer_choice)

    else:
        print("Invalid input. Please type '1' to create a customer or '2' to update a customer.")








