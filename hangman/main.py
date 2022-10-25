import re
import random

# Get the answer
pool_file = open("hangman-sample-answer-pool.txt")

pool_answers = []

pool_answer_line = pool_file.readline()

while pool_answer_line:
    pool_answers.append(pool_answer_line)

    pool_answer_line = pool_file.readline()

pool_file.close()

answer = random.choice(pool_answers)

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

    print("Guessed letters: ", end="")

    for current_letter_guessed in letters_guessed:
        print(current_letter_guessed, end=" ")

    print()

    #display puzzel boeard
    for current_answer_index in range(len(answer)):
        if answer_guessed[current_answer_index]:
            print(answer[current_answer_index], end="")
        else:
            print("_", end="")
    
    print()

    #let user guess a letter
    letter = input("Enter a letter: ")

    letter = letter.upper()

    #check if user entered a valid letter
    if re.search("^[A-Z]$", letter) and len(letter) == 1 and letter not in letters_guessed:
        #insert the letter guessed by the user (insersion sort)
        current_letter_index = 0

        for current_letter_guessed in letters_guessed:
            if letter < current_letter_guessed:
                break

            current_letter_index += 1
        
        letters_guessed.insert(current_letter_index, letter)

        #check if letter is in the puzzle
        if letter in answer:
            for current_answer_index in range(len(answer)):
                if letter == answer[current_answer_index]:
                    answer_guessed[current_answer_index] = True
        else:
            current_incorect_guesses += 1

#post-game summary
if current_incorect_guesses < num_of_incorect_guesses:
    print("Congratulations, you won!")
else:
    print(f"Sorry you lost the answer was  {answer}")