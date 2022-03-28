from full_name_func import full_name

print('Please enter q for quite from program')
while True:
    first = input('Enter your first name\n')
    if first == 'q':
        break

    last_name = input('Enter your last name\n')
    if last_name == 'q':
        break

    formed_name = full_name(first, last_name)
    print(formed_name)

