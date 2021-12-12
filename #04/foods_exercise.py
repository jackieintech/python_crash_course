my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

print("\nMy favorite foods are:")
for mine in my_foods[:4]:
	print(mine.title())

print("\nMy friend's favorite foods are:")
for his in friend_foods[:4]:
	print(his.title())