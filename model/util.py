import random
import string


def generate_id():
    ID = ["A", "A", "A", "A", "A", "-", "A", "A", "A", "A",]
    newID = []
    for ele in ID:
        if ele != "-":
            ele = random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase + string.punctuation)
            while ele == ";":
                ele = random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase + string.punctuation)
            else:
                newID.append(ele)
        elif ele == "-":
            newID.append("-")
    return "".join(newID)
