favorite_places = {'nine': ['new york','london','montclair','paris'],
	'fer' : ['rio', 'new york', 'bogotá'],
	'eve' : ['miami', 'boston'],
	}

for person, places in favorite_places.items():
	print(person)
	print(places)
	for place in places:
		print(f"One of {person.title()}'s favorite places is {place.title()}.")

