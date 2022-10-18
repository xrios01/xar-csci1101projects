import re

# Get the answer
answer = "What's up, Doc?"

answer = answer.upper()

# pe-game set up
answer_guessed = []

for current_answer_character in answer:
    if re.search("^[A-Z]$", current_answer_character):
        answer_guessed.append(False)
    else:
        answer_guessed.append(True)

# game logic
num_of_incorect_guesses = 5

current_incorect_guesses = 0

letters_guessed = []

# user gameplay logic
while current_incorect_guesses < num_of_incorect_guesses and False in answer_guessed:
    # display game summary
    print(f"Number of incorect guesses remaining: {num_of_incorect_guesses - current_incorect_guesses}") 