magicians = ['alice', 'quentin', 'elliott', 'janet', 'josh', 'margot']
for magician in magicians:
	print(f"{magician.title()}, that was a great trick!")

magicians_start = magicians[:3]
print(f"My three favorites magicians are {magicians_start}")

magicians_middle = magicians[2:4]
print(f"Two magicians from the middle are {magicians_middle}.")

magicians_end = magicians[4:]
print(f"The last two are {magicians_end}")