ages = [1, 3, 6, 13, 40, 66]
for age in ages:
    if age < 2:
        print('Person is baby')
    elif age >= 2 and age <= 4:
        print('Person is toddler')
    if age >= 4 and age <= 13:
        print('Person is kid')
    elif age >= 13 and age <= 20:
        print('Person is teenager')
    if age >= 20 and age <= 65:
        print('Person is adult')
    elif age > 65:
        print('Person is elder')
