import random

random_number = random.randint(1,20)

def check_number(number):
    if number != random_number:
        return False
    else:
        return True
