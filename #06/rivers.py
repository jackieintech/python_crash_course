rivers = {
    'nile' : 'egypt',
    'seine' : 'france',
    'hudson' : 'the united states',
    }

for river, country in rivers.items():
    print(f"The {river.title()} is in {country.title()}.")

for river in rivers.keys():
    print(river.title())

for country in rivers.values():
    print(country.title())