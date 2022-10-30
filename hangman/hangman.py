import random
import sys

word_list = ['python', 'java', 'javascript', 'php']
print("HANGMAN")
ATTEMPT = 8


def game():
    random_word = random.choice(word_list)
    word_recognised = "-" * len(random_word)  # variable for "----"
    print("Your word | " + word_recognised)
    answered_letters = ""  # variable for unsweared letters in word word_recognised
    letters_array = []  # array
    def func_attempts():
        if ATTEMPT > 0:
            def letter_recognition(letter): # function fot letter recogition process
                nonlocal word_recognised, letters_array
                free_word = word_recognised # assign recognised letters
                if letter == letter.capitalize(): # check if letter not capitalized
                    print("Please enter a lowercase English letter.")
                    letter_recognition(input("Input your letter "))
                if len(letter) >= 2: # check if user entered single letter
                    print("You should input a single letter.")
                    letter_recognition(input("Input your letter "))
                if letter in random_word: # check if letter located in [randomword]
                    nonlocal answered_letters, letters_array
                    global ATTEMPT
                    if letter in answered_letters:  # check if letter located in word
                        print("Left " + str(ATTEMPT) + " attempts!")
                        print(free_word)
                        if letter in letters_array:
                            print("You've already guessed this letter.")
                        else:
                            letters_array.append(letter)
                            ATTEMPT -= 1
                            print("No improvements!")
                        func_attempts()
                    letter_index_stack = []   # Array for index of letters
                    for i in range(len(random_word)): # loop to find letters index in word
                        if random_word[i] == letter:
                            letter_index_stack.append(i)
                    b = 0
                    while b < len(letter_index_stack):  # loop to find and change letters
                        if letter_index_stack == 0:
                            indexcut = 0
                        else:
                            indexcut = 1
                        free_word = free_word[:(letter_index_stack[b])] + letter\
                                    + free_word[letter_index_stack[b] + indexcut:]
                        word_recognised = word_recognised = free_word
                        b += 1
                    if word_recognised == random_word: # check if user recognised word
                        print("The word is " + free_word + "\nYou won!")
                        game()
                    else:
                        print(word_recognised)
                        letter_recognition(input("Input your letter "))
                    letters_array.append(letter)
                else:
                    if letter in letters_array:
                        print("Left " + str(ATTEMPT) + " attempts!")
                        print(f"""You've already guessed this letter! Try something else
{free_word}""")
                        func_attempts()
                    else:
                        print("Left " + str(ATTEMPT) + " attempts!")
                        letters_array.append(letter)
                        ATTEMPT -= 1
                        print(f"That letter doesn't appear in the word!\n{free_word}")
                        func_attempts()
                print(free_word)
                letter_recognition(input("Input your letter "))
            letter_recognition(input("Input your letter "))
        else:
            print("No attempts")
            game()
    def user_choice():
        global ATTEMPT
        user_choice = input('Type "play" to play the game, "quit" to quit: ')
        if user_choice == "play":
            # ATTEMPTs = 8
            ATTEMPT = 8
            func_attempts()
        elif user_choice == "quit":
            sys.exit()
        else:
            print("You have typed something wrong")
            user_choice()
    user_choice()
game()
