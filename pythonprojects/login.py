greet = input("do u have a account? (yes/no): ")
accounts = {}

if greet.lower() == "no":
    print("Please create an account first.")
    a = input("enter your username: ")
    b = input("enter your password: ")
    if a in accounts:
        print("Account already exists!")
    else:
        accounts[a] = b
        print("Account created successfully!")
        # After account creation, allow login
        user = input("enter your username to login: ")
        passw = input("enter your password to login: ")
        if user in accounts and accounts[user] == passw:
            print("Login successful!")
        else:
            print("Login failed! Incorrect username or password.")

elif greet.lower() == "yes":
    print("please enter the following details to login")
    user = input("enter your username: ")
    passw = input("enter your password: ")
    if user in accounts and accounts[user] == passw:
        print("Login successful!")
    else:
        print("Login failed! Incorrect username or password.")



