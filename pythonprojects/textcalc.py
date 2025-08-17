number = int(input("Enter your first number"))

number2 = int(input("Enter your second number"))


sign = input("Enter the sign you want to use (+, -, *, /): ")


if sign == "+":
    print("the sum is ", float(number + number2))


elif sign == "-":
    print("the difference is ", float(number - number2))

elif sign == "*":
    print("the product is ", float(number * number2))

elif sign == "/":
    try:
        print("the quotient is ", float(number / number2))
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

else:
    print("Invalid sign! Please use +, -, *, or /.")
    print("Please try again with a valid sign.")





