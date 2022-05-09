from model.crm import crm
from view import terminal as view
from model import util as util


def list_customers():
    # get all cutomers from csv model (create a funtion there for this purpose)
    # print these using terminal.ceva de printat tabel
    # that's all floks!
    customers_list = crm.get_customers()
    view.print_table(customers_list)
    # view.print_error_message("Not implemented yet.")


def add_customer():
    first = crm.get_customers()
    second = first[0]
    new_customer = []
    x = 1
    new_customer.append(util.generate_id())
    for x in range(len(second)-1):
        new_customer.append(input(f'Please write {second[x+1]} :'))
    crm.write_customer(new_customer)


def update_customer():
    view.print_error_message("Not implemented yet.")


def delete_customer():
    first = crm.get_customers()
    select = input("Please write user ID: ")
    selected_unit = 0
    for ele in first:
        if str(select) == str(ele[0]):
                break
        else:
            selected_unit += 1
    crm.delete_customer(selected_unit-1)


def get_subscribed_emails():
    
    customers_list_subscribed = crm.get_emails(sub=1)
    view.print_table(customers_list_subscribed)


def run_operation(option):
    if option == 1:
        list_customers()
    elif option == 2:
        add_customer()
    elif option == 3:
        update_customer()
    elif option == 4:
        delete_customer()
    elif option == 5:
        get_subscribed_emails()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List customers",
               "Add new customer",
               "Update customer",
               "Remove customer",
               "Subscribed customer emails"]
    view.print_menu("Customer Relationship Management", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
