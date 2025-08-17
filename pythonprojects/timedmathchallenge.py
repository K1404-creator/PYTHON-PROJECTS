import random
import time


OPERATORS = ["+", "*", "-"]
min_operand = 3

max_operand = 14

TOTAL_PROB = 10


def generate_probelm():
    left = random.randint(min_operand,max_operand)
    right = random.randint(min_operand,max_operand)


    operator = random.choice(OPERATORS)


    expr = str(left) + " " + operator + " " + str(right)

    answer = eval(expr)


    return expr, answer



wrong = 0

input("Press enter to start")


print("--------------")


start_time = time.time()


for i in range(TOTAL_PROB):
    expr, answer = generate_probelm()

    while True:
        guess = input("Problem" + " " + expr  + " = ")
        if guess == str(answer):
            break
        wrong += 1


end_time = time.time()

total_time = round(end_time - start_time, 2)  

print("----------------")
print("You finished in ", total_time, "seconds!")

