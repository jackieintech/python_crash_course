cities = {
    'são paulo' : {
        'country' : 'brazil', 
        'population' : 12000000, 
        'fact' : 'PSDB is king'
        },

    'new york' : {
        'country': 'the united states',
        'population' : 8000000,
        'fact' : 'it never sleeps'
        },
    
    'montclair': {
        'country' : 'the united states',
        'population' : 38000,
        'fact' : 'it is among the wealthiest in the country'
        },
    }

for city_name, city_details in cities.items():
   print(f"\n{city_name.title()}")
   for city_info, city_answers in city_details.items():
    print(f"\t{city_info.title()}: {city_answers}.")