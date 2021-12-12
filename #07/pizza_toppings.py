prompt = "\nWhat would you like to add to your pizza today? "
prompt += "\nEnter 'done' when you're finished selecting your toppings."

active = True
while active:
    topping = input(prompt)
    if topping == 'quit' :
        active = False
    else:
        print(f"Added {topping} to your pizza!")