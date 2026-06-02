import random
from typing import Set, List

def select_random_word() -> str:
    """Selects and returns a word from a predefined list of 5 words."""
    # Predefined list of 5 words as per internship specifications
    word_list: List[str] = ["python", "software", "developer", "internship", "automation"]
    return random.choice(word_list)

def display_game_status(secret_word: str, guessed_letters: Set[str], incorrect_left: int) -> bool:
    """
    Displays the current progress of the hidden word and game statistics.
    Returns True if the word has been completely guessed (victory condition).
    """
    print("\n" + "-" * 50)
    
    # Build the display string (e.g., "p y _ t _ o n")
    displayed_word = [letter if letter in guessed_letters else "_" for letter in secret_word]
    print(f"Word to guess :  {' '.join(displayed_word)}")
    print(f"Attempts left :  {incorrect_left} / 6")
    print(f"Guessed letters:  {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
    
    return "_" not in displayed_word

def get_valid_input(guessed_letters: Set[str]) -> str:
    """Prompts the user for input and ensures it is a valid, un-guessed single alphabet."""
    while True:
        guess = input("Guess a letter: ").lower().strip()
        
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Invalid input. Please enter a single alphabetical character.")
            continue
        if guess in guessed_letters:
            print(f"⚠️ You have already guessed '{guess}'. Try another letter.")
            continue
            
        return guess

def play_hangman() -> None:
    """Executes the main control loop for the text-based Hangman game."""
    print("==================================================")
    print("         WELCOME TO CODEALPHA HANGMAN GAME        ")
    print("==================================================")
    
    secret_word: str = select_random_word()
    guessed_letters: Set[str] = set()
    incorrect_guesses_left: int = 6  # Maximum allowable incorrect entries
    
    while incorrect_guesses_left > 0:
        # Check victory state while printing the current board status
        is_won = display_game_status(secret_word, guessed_letters, incorrect_guesses_left)
        
        if is_won:
            print("\n" + "=" * 50)
            print("🎉 CONGRATULATIONS! You successfully guessed the word! 🎉")
            print("==================================================")
            break
            
        # Retrieve sanitized user input
        guess = get_valid_input(guessed_letters)
        guessed_letters.add(guess)
        
        # Process guess outcome
        if guess in secret_word:
            print(f"✅ Correct! '{guess}' is in the word.")
        else:
            print(f"❌ Incorrect. '{guess}' is not in the word.")
            incorrect_guesses_left -= 1
            
    else:
        # Executes only if the while loop expires naturally (incorrect_guesses_left == 0)
        print("\n" + "=" * 50)
        print("💥 GAME OVER! You have run out of available guesses.")
        print(f"The correct word was: '{secret_word.upper()}'")
        print("==================================================")

if __name__ == "__main__":
    play_hangman()
