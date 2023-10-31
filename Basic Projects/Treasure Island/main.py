from logo import art

print(art)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

option1 = input("You're at crossroads. Do you want to go left or right? type 'left' or right' \n").lower()
if option1 == "left":
    option2 = input("You've come to a lake. Do you want to swim or wait for a boat? type 'swim' or 'wait' \n").lower()
    if option2 == "wait":
        option3 = input(
            "A boat has take you to an island with three doors. which door do you want go into? type 'red' or "
            "'yellow' or 'blue' \n").lower()
        if option3 == "red":
            print("Burned by fire. Game Over")
        elif option3 == "yellow":
            print("You found the treasure! You Win!")

        elif option3 == "blue":
            print("Eaten by beats. Game over")

        else:
            print("You choose a door that doesn't exist. Game over")
    else:
        print("Attacked by trout. Game over")


else:
    print("You fell into a hole. Game Over")
