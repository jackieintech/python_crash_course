pet_0 = {'name' : 'tuka', 'owner': 'sonia', 'kind' : 'dog', 'color' : 'black', 
	'age' : 10,}
pet_1 = {'name' : 'margot', 'owner' : 'lara', 'kind' : 'cat', 'color': 'white', 
	'age' : 2,}
pet_2 = {'name' : 'nemo', 'owner' : 'no one', 'kind' : 'fish', 'color' : 
	'orange', 'age' : 1,}
pet_3 = {'name': 'godofredo', 'owner': 'jaqueline', 'kind' : 'mouse', 'color' :
	 'pink', 'age' : 0,}

pets = [pet_0, pet_1, pet_2, pet_3]
print(pets)

for pet in pets:
	print(f"The pet's name is {pet['name'].title()}.")
	print(f"This is {pet['owner'].title()}'s {pet['kind']}.")
	print(f"It is {pet['color']}.\n")