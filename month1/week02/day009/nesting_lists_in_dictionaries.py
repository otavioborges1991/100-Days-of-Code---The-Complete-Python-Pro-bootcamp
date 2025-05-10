capitals = {
    "France": 'Paris',
    'Germany': 'Berlin',
}

travel_log = {
    'France': ['Paris', 'Lille', 'Dijon'],
    'Germany': ['Stuttgart', 'Berlin'],
    'Brazil': ['Joinville', 'São Paula', 'Florianopolis']
}


for item in travel_log.items():
    print(item)

print(travel_log['France'][1])

countries = {
    'Brazil': {
        'visited': 'live',
        'cities': ['Joinville', 'Florianopolis'],
    },
    'Germany': {
        'visited': 0,
        'cities': 'none',
    },
}

print('Printing countries')
for country in countries:
    print(countries[country])

