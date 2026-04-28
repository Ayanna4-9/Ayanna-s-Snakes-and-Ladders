import random

SNAKES = {16: 6, 48 :30}

LADDERS = {3: 22, 20: 38}

BOARD_END = 100

def apply_snakes_and_ladders(position):
    """
    Check if the current position is a snake head or ladder bottom.
    Return the new position after applying the effect.
    """
    if position in SNAKES:
        print(f"  Oh no! Bitten by a snake at {position}, sliding down to {SNAKES[position]}!")
        return SNAKES[position]
    if position in LADDERS:
        print(f"  Nice! Found a ladder at {position}, climbing up to {LADDERS[position]}!")
        return LADDERS[position]
    return position


def roll_dice():
    """
    Simulate rolling a six-sided dice.
    """
    return random.randint(1, 6)


def take_turn(player_name, current_position):
    """
    Handle a single player's turn:
    - Ask to roll
    - Move
    - Apply snakes/ladders
    - Handle overshoot of 100
    """
    input(f"\n{player_name}, press Enter to roll the dice...")
    dice_value = roll_dice()
    print(f"{player_name} rolled a {dice_value}.")

    tentative_position = current_position + dice_value

    if tentative_position > BOARD_END:
        print(f"  You need exactly {BOARD_END} to win. Staying at {current_position}.")
        return current_position

    print(f"  Moving from {current_position} to {tentative_position}.")
    new_position = apply_snakes_and_ladders(tentative_position)
    print(f"  {player_name} is now at position {new_position}.")
    return new_position


def get_player_names():
    """
    Get valid, non-empty names for Player 1 and Player 2.
    """
    while True:
        p1 = input("Enter name for Player 1: ").strip()
        p2 = input("Enter name for Player 2: ").strip()

        if not p1 or not p2:
            print("Player names cannot be empty. Please try again.\n")
            continue

        if p1 == p2:
            print("Player names must be different. Please try again.\n")
            continue

        return p1, p2


def play_game():
    """
    Main game loop for two players.
    """
    print("=== Snake & Ladder Game (2-Player, Terminal-Based) ===")
    print("First to reach exactly 100 wins.")
    print("Snakes:", SNAKES)
    print("Ladders:", LADDERS)
    print()

    player1, player2 = get_player_names()

    positions = {player1: 1, player2: 1}

    current_player = player1

    while True:
        print("\n----------------------------------------")
        print(f"Current positions: {player1} -> {positions[player1]}, {player2} -> {positions[player2]}")
        print("----------------------------------------")

        positions[current_player] = take_turn(current_player, positions[current_player])

        if positions[current_player] == BOARD_END:
            print(f"\n🎉 {current_player} has reached {BOARD_END} and wins the game! 🎉")
            break

        # Alternate turns
        current_player = player2 if current_player == player1 else player1

    print("\nGame over. Thanks for playing!")


def ask_play_again():
    """
    Ask the user if they want to play again. Validate input.
    """
    while True:
        choice = input("\nDo you want to play again? (y/n): ").strip().lower()
        if choice in ("y", "yes"):
            return True
        if choice in ("n", "no"):
            return False
        print("Invalid input. Please enter 'y' or 'n'.")


def main():
    """
    Entry point of the program.
    """
    while True:
        play_game()
        if not ask_play_again():
            print("Exiting the game. Goodbye!")
            break


if __name__ == "__main__":
    main()