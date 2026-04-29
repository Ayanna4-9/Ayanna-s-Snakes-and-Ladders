# Ayanna-s-Snakes-and-Ladders

Snake & Ladder Game (2‑Player, Terminal-Based)
A simple, interactive, terminal-based implementation of the classic Snake & Ladder board game for two players. Players take turns rolling a dice, climbing ladders, sliding down snakes, and racing to reach exactly 100.

Features
Two-player turn‑based gameplay

Dice roll simulation using random.randint(1, 6)

Snakes and ladders implemented using dictionaries

Input validation for player names and replay prompts

Enforces “must land exactly on 100 to win” rule

Allows replaying multiple rounds

Clean, modular code using functions

Game Rules
Both players start at position 1

On each turn, a player rolls a dice (1–6)

Landing on a ladder bottom moves the player up

Landing on a snake head moves the player down

Players may share the same cell

A player must roll the exact number needed to reach 100

First player to reach 100 wins

Project Structure
Code
SnakeAndLadder/
│── snake_ladder.py        # Main game file
│── README.md              # Project documentation
│── report.pdf/.docx       # Final project report (submitted separately)
How to Run the Program
Requirements
Python 3.x installed

No external libraries required

Run the game
Open a terminal in the project folder and run:

Code
python3 snake_ladder.py
Follow the on‑screen prompts to enter player names and take turns rolling the dice.

Data Structures Used
Snakes
python
snakes = {16: 6, 48: 30}
Ladders
python
ladders = {3: 22, 20: 38}
Player Positions
A dictionary mapping each player's name to their current board position.

Code Organization
The program is broken into clear, reusable functions:

roll_dice() – simulates dice roll

apply_snakes_and_ladders() – checks for snake/ladder interactions

take_turn() – handles a full player turn

get_player_names() – validates player names

play_game() – main game loop

ask_play_again() – replay prompt

main() – entry point

Edge Case Handling
Prevents overshooting 100

Validates player names (non‑empty, unique)

Validates replay input (y/n)

Handles snake/ladder interactions automatically

Possible Improvements
Add more snakes and ladders

Add support for more than two players

Add statistics (how many turns to reach 100 and how many snakes or ladders are encountered)
