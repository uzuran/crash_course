def city_country(city, country):
    all_in_one = city + ' ,' + country
    return all_in_one.title()


while True:
    print('Please tell me your City and country ')
    print('Or you can end application by press "q"')

    f_city = input('City: ')
    if f_city == 'q':
        break
    s_country = input('Country: ')
    if s_country == 'q':
        break

    all_end = city_country(f_city, s_country)
    print(all_end)
    if all_end == all_end:
        break
