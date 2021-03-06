# game.py

import random
import os
from dotenv import load_dotenv

load_dotenv() #> loads contents of the .env file into the script's environment

z = os.getenv("USER_NAME")

print(z) # reads the variable from the environment
#> "Hello World"



#exit()








print("Rock, Paper, Scissors, Shoot!")

#
# ASK FOR A USER INPUT
# source: https://docs.python.org/3/library/functions.html#input
#s = input('--> ')

x = input("Please choose one of 'rock', 'paper', 'scissors': ")
print(x)

x = x.lower()
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


#print("YOU WON")

#print("COMPUTER WON")

# shared by Andrew via Slack
# if x == c:
#     print("It's a tie, try again")
# elif x == "rock" and c == "paper":
#     print ("You Lose! Play again")
# elif x ==  "rock" and c == "scissors":
#     print ("You win! Yay!")
# elif x == "paper" and c == "rock":
#     print ("you win! Yay!")
# elif x == "paper" and c == "scissors":
#     print ("You lose! Better luck next time.")
# elif x == "scissors" and c == "rock":
#     print ("You lose! Sorry!")
# elif x == "scissors" and c == "paper":
#     print ("You win! Yay!")

# alternative dictionary-based approach!!!

winners = {
    "rock": {
        "rock": None,
        "paper": "paper",
        "scissors": "rock",
    },
    "paper": {
        "rock": "paper",
        "paper": None,
        "scissors": "scissors",
    },
    "scissors": {
        "rock": "rock",
        "paper": "scissors",
        "scissors": None,
    }
}

winner = winners[x][c]
if winner == x:
    print("YOU WON!")
elif winner == c:
    print("YOU LOST")
else:
    print("TIE")
