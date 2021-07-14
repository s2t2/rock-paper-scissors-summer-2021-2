# rock-paper-scissors-summer-2021-2

A game of rock, paper, scissors!

## Prerequisites

You should have installed Python version 3.8+.

## Setup

Clone this repo onto your local machine, then navigate to it from the command-line:

```sh
cd /path/to/rock-paper-scissors-summer-2021-2
```

Setup / activate a virtual environment:

```sh
conda create -n my-game-env python=3.8
conda activate my-game-env
```

Install package dependencies:

```sh
pip install -r requirements.txt
```

Create a file called ".env" in the root directory of the local repo, and place inside contents like the following (to customize the player name):

```sh
USER_NAME="Your Name"
```

## Usage

Run the game:

```sh
python game.py
```
