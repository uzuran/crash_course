def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()


while True:
    print('\nPlease tell me your name:')
    print('(q to any time you wont ot quit)')

    f_name = input('First name\n')
    if f_name == 'q':
        break
    l_name = input('Last name\n')
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name)

    print(f'\nHello {formatted_name}')
    if formatted_name == formatted_name:
        break
