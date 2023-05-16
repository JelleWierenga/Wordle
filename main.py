import random

def reveal_word(hidden_word):
    print(f"The hidden word was '{hidden_word}'.")

def show_guessed_words(guessed_words):
    if guessed_words:
        print("Words already guessed:")
        for word in guessed_words:
            print(word)
    else:
        print("No words have been guessed yet.")

score = 0
with open("words.txt") as file:
    word_list = [line.strip() for line in file.readlines()]

hidden_word = random.choice(word_list)
guessed_words = []

while score < 10:
    guess = input("Your guess (type 'stop' to end the game, or 'see words' to view guessed words): ")

    if guess.lower() == "stop":
        reveal_word(hidden_word)
        break

    if guess.lower() == "see words":
        show_guessed_words(guessed_words)
        continue

    if guess in guessed_words:
        print("You've already guessed that word. Try again.")
        continue

    if guess == hidden_word:
        score += 1
        print(f"Congratulations! You guessed the word. The word was '{hidden_word}', and your score is {score}.")
        break
    else:
        guessed_words.append(guess)
        score += 1

        right_place = 0
        right_letters = []
        wrong_place = 0
        wrong_letters = []

        for i in range(len(guess)):
            if guess[i] == hidden_word[i]:
                right_place += 1
                right_letters.append(guess[i])
            elif guess[i] in hidden_word:
                wrong_place += 1
                wrong_letters.append(guess[i])

        print(f"Try again. {right_place} letter(s) in the correct place: {', '.join(right_letters)}")
        print(f"{wrong_place} letter(s) in the wrong place: {', '.join(wrong_letters)}")

if score == 10:
    print(f"You're out of guesses. The hidden word was '{hidden_word}'.")
