# We are going to write a program that generates a random number and asks the user to guess it.
# If the player’s guess is higher than the actual number, the program displays “Lower number please”. 
# Similarly, if the user’s guess is too low, the program prints “higher number please” 
# When the user guesses the correct number, the program displays the 
# number of guesses the player used to arrive at the number.                   DATE : 1 FEB 2025
# Hint: Use the random module.                              Starting time : 7:30pm || Completion time : 8:10pm


#####################################################################################################################################################

import random                                                                          # importing random module

#####################################################################################################################################################

print("⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐")

difficulty = input("ENTER DIFFICULTY FOR THE GAME \n E for easy / M for medium / H for hard / X for extreme --> ")

print("⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐\n")

difficulty_number = 0                                    # number limit that is to be used as diffculty

if difficulty == "E":

    print("YOU CHOSE EASY -_- ")

    difficulty_number = 50

elif difficulty == "M":

    print("YOU CHOSE MEDIUM  :] ")                       # rules for choosing difficulty

    difficulty_number = 100

elif difficulty == "H":

    print("YOU CHOSE HARD ^_^ ")

    difficulty_number = 200

elif difficulty == "X":

    print("YOU CHOSE Xtreme '-' ")

    difficulty_number = 1000

else:

    print("SOMETHING WENT WRONG")


#####################################################################################################################################################

if difficulty == "E" or difficulty == "H" or difficulty == "M" or difficulty == "X":
    
    actual_num = random.randint(1,difficulty_number)                                         # genrating random numbers 

    guess_times = 1                                                                          # intialising variable counter stores times of guesses

    guess_num = 0                                                                            # the number that store value for number used for guessing
 
#####################################################################################################################################################


if difficulty == "E" or difficulty == "H" or difficulty == "M" or difficulty == "X":
    while(True):                                                                             # infinte while loop for program

        print("⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐")

        guess_num = int(input("\nENTER YOUR NUMBER : "))                                     # taking number from the user

        print("⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐")

        guess_times += 1

        if guess_num == actual_num:

             print(f"YOU GUESSED IT !! THE NUMBER {actual_num} in {guess_times} attempts")

             break
        elif guess_num>actual_num:

            print(F"ENTERED NUMBER {guess_num} IS LARGER THAN ACTUAL NUMBER")               # conditions for the games
        
        elif guess_num<actual_num:

            print(F"ENTERED NUMBER {guess_num} IS SMALLER THAN ACTUAL NUMBER")


        else :
             print("SOMETHING WENT WRONG")
             break


#####################################################################################################################################################

print("⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐\n")

print("THANKS FOR PLAYING THE GAME :)")                                                 # good bye

print("⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐⁐\n")

#####################################################################################################################################################
