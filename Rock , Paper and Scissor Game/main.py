# this is going to be my first project i am so excited.               Starting Date : 16 jan 2025 time : 11:47 PM

# ROCK , PAPER AND SCISSOR GAME IN PYTHON                        Date of Completion : 17 jan 2023 time : 01:11 AM

# rock     = "R"                            comp player
# scissor  = "S"
# paper    = "P"                            player computer

#####################################################################################################################################################

import random                    # importing radom module for computer choice

choices = ["R","S","P"]          # computer choices

#####################################################################################################################################################

def game(comp,player):           # actual game code 
    
    if(comp == player):
        print("⟪⟪ Its a Draw 🤷‍♂️ ⟫⟫")

    elif((comp == "R" and player == "S") or (comp == "S" and player == "P") or (comp == "P" and player == "R")):
        print("⟪⟪⟪ YOU LOST THE GAME 😒 ⟫⟫⟫")

    elif((player == "R" and comp == "S") or (player == "S" and comp == "P") or (player == "P" and comp == "R")):
        print("⟪⟪⟪ YOU WON THE GAME 😊 ⟫⟫⟫")
    else:
        print("⟪ SOMETHING WENT WRONG 😱 ⟫")

#####################################################################################################################################################
                                                       
                                                       # printing starting interface
print("""
      
  ⟬⟬⟬⟦⟦ ROCK , PAPER AND SCISSOR GAME IN PYTHON ⟧⟧⟭⟭⟭

     🪨🪨🪨  Choose "R" for Rock   🪨🪨🪨
      
     🧻🧻🧻  Choose "P" for Paper  🧻🧻🧻
      
     ✂️✂️✂️ Choose "S" for Scissor ✂️✂️✂️
      
      """)

#####################################################################################################################################################

times = int(input("HOW MANY ROUNDS YOU WANT TO PLAY » ")) # number for time game repeats

counter = 1

while(counter<times+1):                                   # while loop for game repeation

    print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")

    player = input("ENTER YOUR CHOICE » ")

    comp = random.choice(choices)

    print(f"⟪⟪⟪ You Chose {player} and Computer chose {comp} ⟫⟫⟫")

    game(comp,player)
    
    print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")
    counter += 1
     
#####################################################################################################################################################

print("⟪⟪⟪ THANKYOU FOR PLAYING ⟫⟫⟫\n \t \t- Created by Gurkirat Singh") # outro

#####################################################################################################################################################

# note :-

# this is for future gurkirat
# hey buddy i hope you are well this is you first project
# god is with you dont lose hope
# wishes a best of luck gurkirat !