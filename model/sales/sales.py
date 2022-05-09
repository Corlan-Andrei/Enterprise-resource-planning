""" Sales module

Data table structure:
    - id (string)
    - customer id (string)
    - product (string)
    - price (float)
    - transaction date (string): in ISO 8601 format (like 1989-03-21)
"""

from model import data_manager, util


DATAFILE = "model/sales/sales.csv"
HEADERS = ["Id", "Customer", "Product", "Price", "Date"]


def get_sales():
    result = data_manager.read_table_from_file(DATAFILE)
    return [HEADERS] + result


def write_transaction(sale):
    file = open(DATAFILE, 'a')
    final = ";".join(sale)
    file.write("\n" + final)


def delete_sale(selected_unit):
    with open(DATAFILE, 'r') as file:
        lines = file.readlines()
    with open(DATAFILE, 'w') as file2:
        for index in enumerate(lines):
            if selected_unit != index[0] :
                file2.write(index[1])


def sales_transactions():
    maxim = []
    result = []
    templist = []

    with open(DATAFILE, 'r') as file:
        lines = file.readlines()
        for ele in lines:
            position = ele.split(";")
            templist.append(position[3])
        maxim.append(str(max(templist)))
    return maxim


def expensive_products():
    mult1 = []
    templist_prod = []
    templist_price = []
    objects = []
    prices = []
    rezult = ["1"]

    with open(DATAFILE, 'r') as file:
        lines = file.readlines()
        for ele in lines:
            position = ele.split(";")
            templist_prod.append(position[2])
        for ele in lines:
            position = ele.split(";")
            templist_price.append(position[3])

    for x in templist_prod:
        if str(x) not in objects:
            objects.append(str(x))
    for ele in objects:
        occurrences = templist_prod.count(ele)
        mult1.append(str(occurrences))

    for x in templist_price:
        if str(x) not in prices:
            prices.append(str(x))
    
    var1 = 0
    var2 = [0]
    
    for x in range(len(objects)):
        var1= float(prices[x])*float(mult1[x])

        if var1 > float(var2[0]):
            var2[0] = var1
            rezult[0] = objects[x]  #is the rezul here a typo error?
    return rezult
    
        
#2 =products
#3 =Price

def transaction_sum(trans1, trans2):
    final = 0
    values = []
    with open(DATAFILE, 'r') as file:
        lines = file.readlines()
        for ele in lines:
            position = ele.split(";")
            if str(position[4]) >= str(trans1) and str(position[4]) <= str(trans1) :
                values.append(position[3])
    for element in values:
        final = final + float(element)
    return final

