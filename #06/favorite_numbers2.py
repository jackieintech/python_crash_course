favorite_numbers = {
    'jaqueline' : [11, 2, 200],
    'freddy' : [13, 45, 17], 
    'taylor': [1989, 1000000], 
    'adele' : [19, 21],
    'andrew' : [0, 1111],
    }

favorite_number_0 = favorite_numbers['jaqueline']
print(f"Jaqueline's favorite number is {favorite_number_0}.")

favorite_number_1 = favorite_numbers['freddy']
print(f"Freddy's favorite number is {favorite_number_1}.")

favorite_number_2 = favorite_numbers['taylor']
print(f"Taylor's favorite number is {favorite_number_2}.")

favorite_number_3 = favorite_numbers['adele']
print(f"Adele's favorite number is {favorite_number_3}.")

favorite_number_4 = favorite_numbers['andrew']
print(f"Andrew's favorite number is {favorite_number_4}.")

for name, numbers in favorite_numbers.items():
    print(f"\nSome of {name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"\t{number}")