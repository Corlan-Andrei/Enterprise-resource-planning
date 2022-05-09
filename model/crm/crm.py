""" Customer Relationship Management (CRM) module

Data table structure:
    - id (string)
    - name (string)
    - email (string)
    - subscribed (int): Is subscribed to the newsletter? 1: yes, 0: no
"""

from model import data_manager, util


DATAFILE = "model/crm/crm.csv"
HEADERS = ["id", "name", "email", "subscribed"]


# make a function to fetch data for listing
# get all things from crm csv file using data_manager
# return them to whoever called us (that function)

def get_customers():
    result = data_manager.read_table_from_file(DATAFILE)
    # pun in fata HEADERS
    # customers.insert(HEADERS, 0)  # not ok to alter the response of another funtion; avoid if possible
    return [HEADERS] + result


def write_customer(customer):
    file = open(DATAFILE, 'a')
    final = ";".join(customer)
    file.write("\n" + final)


def delete_customer(selected_unit):
    with open(DATAFILE, 'r') as file:
        lines = file.readlines()
    with open(DATAFILE, 'w') as file2:
        for index in enumerate(lines):
            if selected_unit != index[0] :
                file2.write(index[1])


def get_emails(sub):
    resulting_list =[]
    with open(DATAFILE, 'r') as file:
        lines = file.readlines()
        for ele in lines:
            position = ele.split(";")
            if str(sub) in position[3] :
                resulting_list.append(position)
    if len(resulting_list) == 0:
            return [HEADERS] + [["0","0","0","0"]]
    else:
        return [HEADERS] + resulting_list