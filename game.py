# this is the game.py file!

import random
import os

from dotenv import load_dotenv

load_dotenv() #> loads contents of the .env file into the environment

USER_NAME = os.getenv("USER_NAME") # reads the variable from the environment

print("Rock, Paper, Scissors, Shoot!")
print("WELCOME", USER_NAME)

#
# ASK FOR A USER INPUT
# see: https://docs.python.org/3/library/functions.html#input
#

user_choice = input("Please choose one of 'rock', 'paper', 'scissors': ")
user_choice = user_choice.lower()
print("USER CHOSE:", user_choice)

#
# VALIDATE THE USER INPUT
#

VALID_OPTIONS = ["rock", "paper", "scissors"] # this is a list

if user_choice not in VALID_OPTIONS:
    print("OOPS, INVALID, PLEASE TRY AGAIN!")
    exit()

#
# GENERATE A COMPUTER CHOICE
# https://docs.python.org/3/library/random.html
# source: https://stackoverflow.com/questions/306400/how-to-randomly-select-an-item-from-a-list
#

computer_choice = random.choice(VALID_OPTIONS)

print("COMPUTER CHOSE:", computer_choice)

#
# DETERMINE THE WINNER
#

WINNERS = {
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

winner = WINNERS[user_choice][computer_choice]

if winner == user_choice:
    print("YOU WON!")
elif winner == computer_choice:
    print("YOU LOST")
else:
    print("TIE")
