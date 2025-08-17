import json


def add_person():
    name = input("Enter the person's name: ")
    age = input("Enter the person's age: ")
    email = input("Enter the person's email: ")


    person = {
        "name": name,
        "age": age,
        "email": email}
    
    return person
# enumerate() allows you to iterate over an iterable (such as a list, tuple, or string) while also keeping track of the index of each item in the iterable.


def display_people(people):
    for i, person in enumerate(people):
        print((i+1), ":", person["name"], "-", person["age"], "-", person["email"])



def delete_person(people):
    display_people(people)

    while True:
        try:
            number = int(input("Enter the number of the person you want to delete: "))
            if number <=0 or number > len(people):
                print("Invalid number. Please try again.")
            else:
                break
        except:
            print("Invalid input. Please enter a valid number.")

    people.pop(number -1)

    print("Person deleted successfully!")


def search_person(people):
    s_name = input ("Enter the name of the person you want to search for:").lower()

    results = []

    for person in people:
        name = person["name"]
        if s_name in name.lower():
            results.append(person)


print("HI WELCOME TO CONTACT MANAGEMENT SYSTEM")

with open("contacts.json", "r") as f:
    people = json.load(f)["contacts"]


while True:
    print("Contact list size", len(people))

    print("Add a person (1) ,  Delete a person (2), Search for a person (3), Exit (4)")

    command = int(input("choice"))

    if command == 1:
        person = add_person()
        people.append(person)
        print("Person added successfully!")

    elif command == 2:
        delete_person(people)
    elif command == 3:
        search_person(people)

    elif command == 4:
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid command. Please try again.")



with open("contacts.json", "w") as f:
    people = json.dump({"contacts": people},f)




    