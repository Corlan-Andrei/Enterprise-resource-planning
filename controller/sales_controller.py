from model.sales import sales
from view import terminal as view
from model import util as util


def list_transactions():
    customers_list = sales.get_sales()
    view.print_table(customers_list)

def add_transaction():
    alist = sales.get_sales()
    value = alist[0]
    new_transaction = []
    x = 1
    new_transaction.append(util.generate_id())
    for x in range(len(value)-1):
        new_transaction.append(input(f'Please write {value[x+1]} :'))
    sales.write_transaction(new_transaction)


def update_transaction():
    view.print_error_message("Not implemented yet.")


def delete_transaction():
    first = sales.get_sales()
    select = input("Please write user ID: ")
    selected_unit = 0
    for ele in first:
        if str(select) == str(ele[0]):
                break
        else:
            selected_unit += 1
    sales.delete_transaction(selected_unit-1)

def get_biggest_revenue_transaction():
    big_money = sales.sales_transactions
    view.print_table(big_money)


def get_biggest_revenue_product():
    print(sales.expensive_products())


def count_transactions_between():
    view.print_error_message("Not implemented yet.")


def sum_transactions_between():
    trans1 = input('Please type in your first date: ')
    trans2 = input('Please type in your last date: ')
    rezult = sales.transaction_sum(trans1, trans2)
    view.print_table(rezult)

def run_operation(option):
    if option == 1:
        list_transactions()
    elif option == 2:
        add_transaction()
    elif option == 3:
        update_transaction()
    elif option == 4:
        delete_transaction()
    elif option == 5:
        get_biggest_revenue_transaction()
    elif option == 6:
        get_biggest_revenue_product()
    elif option == 7:
        count_transactions_between()
    elif option == 8:
        sum_transactions_between()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List transactions",
               "Add new transaction",
               "Update transaction",
               "Remove transaction",
               "Get the transaction that made the biggest revenue",
               "Get the product that made the biggest revenue altogether",
               "Count number of transactions between",
               "Sum the price of transactions between"]
    view.print_menu("Sales", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
