name = input ("Type your name : ")
print("Welcome",name, "to this adventure!")

answer = input(
    "You are on dirty road,it has come to an end and you can go left or right.Which way would you like to go? ").lower()

if answer == "left":
    answer=input("You come to river, you can walk around it or swim accross it?Type walk to walk around and swim to swim accross").lower()
    if answer == "swim":
        print("You swam accross and eaten by an aligatorand you lost the game.")

    elif answer =="walk":
        print("You walked for many mile and ran out of water and you lost the game.")

    else:
        print ("Not valid option you lose.")
elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly do you want to cross it or head back(cross/back)").lower()
    if answer == "back":
        print("You go back and lose.")
    elif answer == "cross":
        answer=input("You cross the bridge and meet a stranger .Do you talk to him? (yes/no)").lower()
        if answer == "yes" :
            print("You talk to stranger and they give you gold.You WIN!")
        elif answer == "no":
            ("You ignore the stranger they offended and kill you.You lose!")
        else:
            print("not a valid option")   


    else:
        print ("Not valid option you lose.")


else:
    print("Not a valid option.You lose.")    
print("Thank you for trying",name,("."))    

