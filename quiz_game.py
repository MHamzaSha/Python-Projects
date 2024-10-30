print("Welcome to my computer quiz")

playing = input("Do you want to play the game? ")
if playing.lower() != "yes":
    quit()

print("Okay! Let's play : )")
score=0

#1st
answer =input("What does CPU stand for? ")
if answer.lower() == ("central processing unit") :
    print ("Correct!")
    score+=1
else:
    print("Incorrrect!")

#2nd
answer =input("What does GPU stand for? ")
if answer.lower() == ("graphics processing unit") :
    print ("Correct!")
    score+=1
else:
    print("Incorrrect!")

#3rd
answer =input("What does ROM stand for? ")
if answer.lower() == ("read only memory") :
    print ("Correct!")
    score+=1
else:
    print("Incorrrect!")

#4th
answer =input("What does PSU stand for? ")
if answer.lower() == ("power supply unit") :
    print ("Correct!")
    score+=1
else:
    print("Incorrrect!")

#5th
answer =input("What does RAM stand for? ")
if answer.lower() == ("random access memory") :
    print ("Correct!")
    score+=1
else:
    print("Incorrrect!")

print("You got "+str(score)+" questions correct.")
print ("You got"+str((score/5)*100)+ "%.")    
