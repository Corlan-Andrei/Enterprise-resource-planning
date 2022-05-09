from model.hr import hr
from view import terminal as view
from model import util as util


def list_employees():
    customers_list = hr.get_employees()
    view.print_table(customers_list)

def add_employee():
    first = hr.get_employees()
    value = first[0]
    new_employee = []
    x = 1
    new_employee.append(util.generate_id())
    for x in range(len(firstish)-1):
        new_employee.append(input(f'Please write {firstish[x+1]} :'))
    hr.write_employee(new_employee)


def update_employee():
    view.print_error_message("Not implemented yet.")
    # sa ne folosim de ID pentru a selecta employee


def delete_employee():
    first = hr.get_employees()
    select = input("Please write user ID: ")
    selected_unit = 0
    for ele in first:
        if str(select) == str(ele[0]):
                break
        else:
            selected_unit += 1
    hr.delete_employee(selected_unit-1)


def get_oldest_and_youngest():
    customers_list = hr.get_age()
    view.print_table(customers_list)
    


def get_average_age():
    view.print_error_message("Not implemented yet.")
    # check against Date of Birth, make average


def next_birthdays():
    view.print_error_message("Not implemented yet.")
    # check against Date of Birth


def count_employees_with_clearance():
    select = input("Please write user clerence: ")
    alist = hr.get_clearence(select)
    view.print_table(alist)


def count_employees_per_department():
    final_list = hr.count_employee()
    view.print_table(final_list)


def run_operation(option):
    if option == 1:
        list_employees()
    elif option == 2:
        add_employee()
    elif option == 3:
        update_employee()
    elif option == 4:
        delete_employee()
    elif option == 5:
        get_oldest_and_youngest()
    elif option == 6:
        get_average_age()
    elif option == 7:
        next_birthdays()
    elif option == 8:
        count_employees_with_clearance()
    elif option == 9:
        count_employees_per_department()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List employees",
               "Add new employee",
               "Update employee",
               "Remove employee",
               "Oldest and youngest employees",
               "Employees average age",
               "Employees with birthdays in the next two weeks",
               "Employees with clearance level",
               "Employee numbers by department"]
    view.print_menu("Human resources", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
