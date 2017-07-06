import random

random_number = random.randint(1,20)

def check_number(number):
    if number != random_number:
        return False
    else:
        return True

def get_input():
    while True:
        guess_input = ''
        try:

            guess_input = int(input())
        except ValueError:
            print("That is not a valid input")
            guess_input = ''

        if guess_input != '':
            return guess_input
            break

def high_low(number):
    if number > random_number:
        print("That is too high guess again")
    elif number < random_number:
        print("That is too low guess again")

counter = 1
while True:
    print('I am thinking of a number can you guess what it is?')
    number = get_input()
    if check_number(number):
        print(f"You are correct and you did it in {counter} guesses")
        break
    else:
        high_low(number)
    counter += 1
