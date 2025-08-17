print("welcome to my quiz")


play = input("Do you want to play? (yes/no): ")

if play.lower()!= "yes":
    quit()

else:
    print("Great! Let's play :)")
    score = 0 

answer = input("what is india's capital? ")

if answer.lower() == "delhi":
    print("Correct!")
    score += 1
else: 
    print("Incorrect! The correct answer is Delhi.")




answer = input("what is usa's capital? ")

if answer.lower() == "washington dc":
    print("Correct!")
    score += 1
else: 
    print("Incorrect! The correct answer is washington dc.")




answer = input("what is japan's capital? ")

if answer.lower() == "tokyo":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is Tokyo.")




print("You got " + str(score) + " out of 3 questions correct.")









