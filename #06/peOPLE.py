person_0 = {'first_name' : 'jaqueline', 'last_name' : 'granja', 'age' : 33, 
	'city' : 'são paulo'}
print(person_0['first_name'])
print(person_0['last_name'])
print(person_0['age'])
print(person_0['city'])

person_1 = {'first_name' : 'rebecca', 'last_name': 'wollman', 'age' : 34, 
	'city' : 'piscataway'}

person_2 = {'first_name' : 'jessica', 'last_name' : 'perry', 'age' : 35, 
	'city' : 'philadelphia'}

people = [person_0, person_1, person_2]

for each in people:
	print(f"\nMy friend's name is {each['first_name'].title()}.")
	print(f"My friend's last name is {each['last_name'].title()}.")	
	print(f"My friend is {each['age']} years old.")
	print(f"My friend lives in {each['city'].title()}.")
