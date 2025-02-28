import random  

def main():
    """
    Main function to run the Number Guesser game.

    The game generates a random number between 1 and 100, and the player has 10 attempts to guess the number.
    The player can input their guess or type 'q' or 'Q' to quit the game.
    The function provides hints if the guess is too high or too low.
    If the player guesses the correct number, they are congratulated and asked if they want to play another round.
    If the player chooses to play again, a new random number is generated and the score is reset to 100.
    If the player inputs an invalid number, they are prompted to guess again.

    Exceptions:
        ValueError: Catches invalid input that cannot be converted to an integer.
    """
    # Generate a random number between 1 and 100
    rand_num = random.randint(1, 100)
    # Initialize the score to 100
    score = 100

    try:
        while True:
            # Prompt the player to guess a number
            input_num = input('Please Guess a Number: ')

            # Check if the player wants to quit
            if input_num.lower() == 'q':
                print('Thanks for Playing!')
                break

            # Validate the input
            if not input_validator(input_num):
                continue

            else:
                input_num = int(input_num)
            # Check if the guessed number is correct
            if input_num == rand_num:
                print(f'Congratulations! You Win with {score} Scores!')
                ans = input('Play for Another Round? (y/n): ')
                # Check if the player wants to play again
                if play_again(ans):
                    rand_num = random.randint(1, 100)
                    score = 100
                else:
                    break

            # Provide hints if the guess is too high or too low
            elif input_num > rand_num:
                print('You guessed too high!')
            else:
                print('You guessed too low!')

            score -= 10
            score = max(score, 0)

    except ValueError:
        pass

def input_validator(input_num):
    """
    Validate the player's input.

    Args:
        input_num (str): The player's input.

    Returns:
        bool: True if the input is valid, False otherwise.
    """
    # Check if the input is a digit
    if not input_num.isdigit():
        print('Please Insert a Valid Number: ')
        return False
    
    input_num = int(input_num)
    
    # Check if the input is within the valid range
    if input_num > 100 or input_num < 1:
        print('Number Must be Between 1 and 100. Try Again: ')
        return False
    
    return True

def play_again(ans):
    """
    Check if the player wants to play again.

    Args:
        ans (str): The player's answer.

    Returns:
        bool: True if the player wants to play again, False otherwise.
    """
    if ans.lower() == 'y':
        return True
    else:
        print('Thanks for Playing!')
        return False

if __name__ == '__main__':
    main()
