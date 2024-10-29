print("Welcome to my computer quiz")

playing = input("Do you want to play the game? ")
if playing != "yes":
    quit()

print("Okay! Let's play : )")

answer =input("What does CPU stand for? ")
if answer in ("central processing unit","Central processsing unit") :
    print ("Correct!")
else:
    print("Incorrrect!")


