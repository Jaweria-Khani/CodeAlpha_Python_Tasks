import random

def display_hangman(attempts):
    stages = [
        '''
           -----
           |   |
           O   |
          /|\  |
          / \  |
               |
        --------
        ''',
        '''
           -----
           |   |
           O   |
          /|\  |
          /    |
               |
        --------
        ''',
        '''
           -----
           |   |
           O   |
          /|\  |
               |
               |
        --------
        ''',
        '''
           -----
           |   |
           O   |
          /|   |
               |
               |
        --------
        ''',
        '''
           -----
           |   |
           O   |
           |   |
               |
               |
        --------
        ''',
        '''
           -----
           |   |
           O   |
               |
               |
               |
        --------
        ''',
        '''
           -----
           |   |
               |
               |
               |
               |
        --------
        '''
    ]
    return stages[attempts]

def hangman():
    words = ['python', 'developer', 'software', 'programming', 'debugging']
    word = random.choice(words)
    guessed_word = ['_'] * len(word)
    attempts = 6
    guessed_letters = []

    print("Welcome to Hangman!")
    print(display_hangman(attempts))
    print("Word:", " ".join(guessed_word))

    while attempts > 0 and "_" in guessed_word:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Please guess a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again!")
            continue

        guessed_letters.append(guess)

        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
            print("Correct!")
        else:
            attempts -= 1
            print("Wrong guess!")
        
        print(display_hangman(attempts))
        print("Word:", " ".join(guessed_word))

    if "_" not in guessed_word:
        print(f"Congratulations! You guessed the word: {word}")
    else:
        print(f"Game Over! The word was: {word}")

if __name__ == "__main__":
    hangman()


