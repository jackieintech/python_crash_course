pizzas = ['vegan', 'cheese', 'mushroom']
for pizza in pizzas:
	print(f"I like {pizza.title()} pizza.")
print("I really love pizza!")

friend_pizzas = pizzas[:]
print(friend_pizzas)

pizzas.append('tomato')
friend_pizzas.append('pepperoni')
print(f"My favorite pizzas are:")
for my_pizza in pizzas[:4]:
	print(my_pizza.title())

print(f"\nMy friend's favorite pizzas are:")
for his_pizza in friend_pizzas[:4]:
	print(his_pizza.title())