# Step 5

import random
import hangman_words
import hangman_art


chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6
print(hangman_art.logo)
# Testing code
print(f'Pssst, the solution is {chosen_word}.')
palavra = []
for _ in range(word_length):
    palavra += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in palavra:
        print(f"You've already guessed {guess}")
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            palavra[position] = letter
    if guess not in chosen_word:
        print(f"The letter {guess} is not in the word. You lose a life.")
        lives -= 1
        print(f"You have {lives} lives left!")
        if lives == 0:
            end_of_game = True
            print("You lose.")
    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(palavra)}")
    if "_" not in palavra:
        end_of_game = True
        print("You win.")
    print(hangman_art.stages[lives])