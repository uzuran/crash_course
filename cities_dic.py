cities = {
    'czech republic': {
        'city': 'prague',
        'interesting': 'charles bridge',
        'population': 1.3,
    },

    'belarus': {
        'city': 'minsk',
        'interesting': 'dictature',
        'population': 1.975
    }
}

for city, info in cities.items():
    print('\n' + city.title() + '\n')
    for i, x in info.items():
        print(i.title() + ' ' + str(x).title())



