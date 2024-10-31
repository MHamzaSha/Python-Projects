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
print(rndm_num)