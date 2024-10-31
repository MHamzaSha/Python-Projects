import random

user_wins=0
computer_wins=0
options = ["rock","paper","scissors"]

while True:
    user_input=input("Type Rock/Paper/Scissors or Q to quit. : ").lower()
    if user_input == "q":
        break
    if user_input not in options:
        continue
    random_num=random.randint(0,2)
    copmuter_pick =options[random_num]
    print("Computer picked",copmuter_pick+".")

    if user_input == "rock" and copmuter_pick =="scissors":
        print("You Won!")
        user_wins+=1

    elif user_input == "paper" and copmuter_pick =="rock":
        print("You Won!")
        user_wins+=1

    elif user_input == "scissors" and copmuter_pick =="paper":
        print("You Won!")

    else:
        print("You Lost!")
        computer_wins+=1

        

print("You won",user_wins,"times.")
print("Computer won",computer_wins,"times.")



print("Goodbye!")


