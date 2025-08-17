import random

user_wins = 0
computer_win = 0


options = ["rock", "paper", "scissor"]
while True:
    user_input = input("type rock paper or scissor or Q to quit").lower()


    if user_input == "q":
        break


    if user_input not in options:
        continue


    random_number = random.randint(0,2)


    computer_pick = options[random_number]
    print("Computer picked", computer_pick)


    if user_input == "rock" and computer_pick == "scissor":
        print("you won!")

        user_wins += 1

    elif user_input == "scissor" and computer_pick == "paper":
        print("you won!")

        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("you won!")

        user_wins += 1

    elif user_input == "paper" and computer_pick == "paper":
        print("tie!")


    elif user_input == "rock" and computer_pick == "rock":
        print("tie")



    elif user_input == "scissor" and computer_pick == "scissor":
        print("tie")



    else:
        print("YOU LOST!")

        computer_win +=1



print("you won ", user_wins , "times")
print("computer won ", computer_win , "times")
print("BYE")