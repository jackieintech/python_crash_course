prompt = "\nHow old are you? "
age = int(input(prompt))
if age < 3 :
    print("Your ticket is free.")
if age <= 12 :
    print("Your ticket is $10.")
if age > 12 :     
    print("Your total is $15.")