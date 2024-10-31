import random
top_of_range=input("Type the number: ")

if top_of_range.isdigit():
    top_of_range=int(top_of_range)
    if top_of_range<=0:
        print("Please type the number larger than 0 next time")
        quit()
else:
    print("Please type a number next time")
    quit()
rndm_num=random.randint(0,top_of_range)
guesses =0

while True :
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Type number next time.")
        continue
    
    if user_guess == rndm_num:
        print("You got it!")
        break
    else:
        if user_guess>rndm_num:
            print("You were above the number!")
        else:
            ("You were below the number!")
guesses = str(guesses)
print ("you guess the number in "+ guesses+" try")