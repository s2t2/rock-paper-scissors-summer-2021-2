# game.py

import random



print("Rock, Paper, Scissors, Shoot!")

#
# ASK FOR A USER INPUT
# source: https://docs.python.org/3/library/functions.html#input
#s = input('--> ')

x = input("Please choose one of 'rock', 'paper', 'scissors': ")
print(x)

# VALIDATE THE USER INPUT

#if x == "rock": # "paper" "scissors"
#    print("VALID")
#else:
#    print("OOPS, INVALID, PLEASE TRY AGAIN")
#    exit()

if (x == "rock") or (x == "paper") or (x == "scissors"):
    print("VALID")
else:
    print("OOPS, INVALID, PLEASE TRY AGAIN")
    exit()

#print("LATER MESSAGES")

print("USER CHOSE: ", x)

# GENERATE A COMPUTER CHOICE
# https://docs.python.org/3/library/random.html
# source: https://stackoverflow.com/questions/306400/how-to-randomly-select-an-item-from-a-list
#
# import random
#
# foo = ['a', 'b', 'c', 'd', 'e']
# print(random.choice(foo))

# more about datatypes lists, and tuples, etc next class
#valid_options = ("rock", "paper", "scissors") # tuple
valid_options = ["rock", "paper", "scissors"] # list

c = random.choice(valid_options)

print("COMPUTER CHOSE:", c)


# DETERMINE THE WINNER
