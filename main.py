import random

score = 0
word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "imbu", "jackfruit", "kiwi", "lemon", "mango", "nectarine", "orange", "papaya", "quince", "raspberry", "strawberry", "tangerine"]
hidden_word = random.sample(word_list, 1)[0]  # Access the first element in the list
guessed_words = []

while score < 10:
    guess = input("Your guess: ")

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
