def city_country(city, country, population=0):
    if population:
        all_in_one = city + ' ' + country + ' ' + str(population)
        return all_in_one.title()
    else:
        all_in_one = city + ' ' + country
        return all_in_one.title()


print(city_country('prague', 'czech republic'))
