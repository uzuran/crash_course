rivers_city = {'nile': 'egypt',
               'river1': 'city1',
               'river2': 'city2',
               'river3': 'city3'}

for river, city in rivers_city.items():
    print('The ' + river.title() + ' runs trough ' + city.title())

print('\nRivers included:\n')

for river in rivers_city:
    print(river.title())

print('\nCity included:\n')

for city in rivers_city.values():
    print(city)
