import random


def load_dictionary(file_path):
    with open(file_path) as f:
        return [line.strip().lower() for line in f]


def is_valid_guess(guess, guesses):
    return len(guess) == 5 and guess in guesses


def evaluate_guess(guess, word):
    result = ""

    for i in range(5):
        if guess[i] == word[i]:
            result += '\033[32m' + guess[i]
        elif guess[i] in word:
            result += '\033[33m' + guess[i]
        else:
            result += '\033[0m' + guess[i]

    return result + '\033[0m'


def wordle(guesses, answers):
    print("Welcome to Wordle! You have 6 attempts to guess a 5-letter word.\n")

    secret_word = random.choice(answers)
    attempts = 1
    max_attempts = 6

    while attempts <= max_attempts:
        guess = input(f"Enter guess #{attempts}: ").lower()

        if not is_valid_guess(guess, guesses):
            print("Invalid guess. Enter a valid 5-letter English word.\n")
            continue

        if guess == secret_word:
            print(f"\nCongrats! You guessed the word: {secret_word}")
            return

        print(evaluate_guess(guess, secret_word))
        attempts += 1

    print(f"\nGame over. The secret word was: {secret_word}")


# Load dictionaries once
guesses = load_dictionary("guesses.txt")
answers = load_dictionary("answers.txt")



while True:
    wordle(guesses, answers)

    again = input("\nPlay again? (y/n): ").lower()
    if again != "y":
        print("Thanks for playing!")
        break