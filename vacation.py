empty_tuple = {}

activate = True

while activate:
    quite = 'For end the program enter quit'
    name = input(f'Hello enter your name: ' + f'\n{quite}')
    if name == 'quit':
        activate = False
    vacation = input('Tel me witch please you wont to visit' + '\n')

    empty_tuple[name] = vacation
    break

for name, vacation in empty_tuple.items():
    print(name + ' Would like visiting : ' + vacation)
