print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

first_choice = input("Which way would you like to"
                     " go first, left or right?\n ").upper()
if first_choice == "LEFT":
    second_choice = input("You survived that section, but we "
                          "will see how you do next! Will you swim or wait?\n ").upper()
    if second_choice == "WAIT":
        third_choice = input("Okay you passed that section, but which "
                             "door will you choose next: Blue, Yellow, or Red?\n ").upper()
        if third_choice == "YELLOW":
            print("You found the treasure! You Win!")
        elif third_choice == "BLUE":
            print("Eaten by beasts. Game Over")
        elif third_choice == "RED":
            print("Burned by fire. Game Over")
        else:
            print("You chose a door that doesn't exist. Game Over")
    else:
        print("Attacked by sharks. Game Over")
else:
    print("Fall into a hole. Game over.")

