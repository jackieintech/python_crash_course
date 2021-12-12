number_of_people = input("How many people will be joining your party?")
print(number_of_people)
number_of_people = int(number_of_people)

if number_of_people > 8:
    print("I'm afraid you'll have to wait for a table.")
else:
    print("Please follow me. Your table is ready.")