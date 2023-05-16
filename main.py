import random
score = 0
word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "imbu", "jackfruit", "kiwi", "lemon", "mango", "nectarine", "orange", "papaya", "quince", "raspberry", "strawberry", "tangerine"]
Hidden_word = random.sample(word_list, 1)[0]

while score < 10:
    guese = input("You're guese: ")
    if guese == Hidden_word:
        score = score + 1
        print(f"congrats you guesed the word! The hidden word was {Hidden_word} and you're score is {score}")
        break
    else:
        print(f"Try again")
        score = score + 1
print(f"You're out of gueses the hidden word was {Hidden_word}")