file = 'guests_names'

while True:
    guests_names = input('Enter your name \n')
    if guests_names == 'q':
        break
    else:
        with open(file, 'w') as file_object:
            file_object.write(guests_names + '\n')

        print(f'Hello {guests_names}')
        continue
