while True:
    print('Give me tow numbers, and i ll divide them')
    print('q to quite.')
    first_number = input('\nFirst number: ')
    if first_number == 'q':
        break
    second_number = input('\nSecond number: ')
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print('You cant divide by 0')
        continue
    else:
        print(answer)

