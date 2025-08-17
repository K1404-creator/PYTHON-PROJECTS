import random
from urllib.parse import uses_relative

# r = random.randrange(-5,11) # excludes 11
#
# r2 = random.randint(-4,11) #includes 11

# print(r)

top_of_range =  input("type a number")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0 :
        print("please enter number greater than 0")
        quit()

else:
    print("please a type a number next time")
    quit()

random_number = random.randint(0, top_of_range)

guesses = 0
while True:
    guesses+= 1
    user_guess = input("Make a guess")

    if user_guess.isdigit():
        user_guess = int(user_guess)



    else:
        print("please a type a number next time")
        continue


    if user_guess == random_number:
        print("You got it")
        break

    elif user_guess > random_number:

        print("above the number")

    else:
        print("below the number")




print("guesses "  , guesses)







