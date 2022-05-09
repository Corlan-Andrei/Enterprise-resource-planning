
# options = ["Exit program",
#                "Customer Relationship Management (CRM)",
#                "Sales",
#                "Human Resources"]
#     view.print_menu("Main menu", options)


def print_menu(title, list_options):
    # Args:
    #     title (str): the title of the menu (first row)
    #     list_options (list): list of the menu options (listed starting from 1, 0th element goes to the end)
    print(title)
    for x, ele in enumerate(list_options[1:], 1):
        print(x, ele)
    print(0, list_options[0])


def print_message(message):
    # """Prints a single message to the terminal.
    # Args:
    #     message: str - the message
    # """
    print(message)


def print_general_results(result, label):
    """Prints out any type of non-tabular data.
    It should print numbers (like "@label: @value", floats with 2 digits after the decimal),
    lists/tuples (like "@label: \n  @item1; @item2"), and dictionaries
    (like "@label \n  @key1: @value1; @key2: @value2")
    """

    # pentru fiecare lement din fiecare element (litera din cuvant) we add "--" ca sa creem lungimea tabelului 
    pass


# /--------------------------------\
# |   id   |   product  |   type   |
# |--------|------------|----------|
# |   0    |  Bazooka   | portable |
# |--------|------------|----------|
# |   1    | Sidewinder | missile  |
# \-----------------------------------/    HEADERS!!!!!
def print_table(table):
    """Prints tabular data like above.

    Args:
        table: list of lists - the table to print out
    """
    # pF5v4wG_e_;Dr. Strangelove;strangelove@rgv453.grer;
    cell_width = 30
    table_start = '/' + ('-' * cell_width) * len(table[0]) + '---\\'
    table_end = '\\' + ('-' * cell_width) * len(table[0]) + '---/'
    horizontal_separator = ('|' + '-' * cell_width) * len(table[0]) + '|'

    print(table_start)
    for row in table:
        row_str = ''
        for cell in row:
            row_str += f'|{cell:^{cell_width}}'
        row_str += '|'
        print(row_str)
        print(horizontal_separator)
    print(table_end)

#    print("\--------------------------------/ ")


def get_input(label):
    user_input = input(">>>")
    return user_input


def get_inputs(labels):
    """Gets a list of string inputs from the user.

    Args:
        labels: list - the list of the labels to be displayed before each prompt
    """
    pass


def print_error_message(message):
    # Args:
    #     message: str - the error message
    print(f' **** {message} ****')


def print_employees(list):
    for item in list[0]:
        print(item, end=" ")
    print("")
    for item in list[1:]:
        for element in item:
            print(element)