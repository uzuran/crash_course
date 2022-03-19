def show_complete_modified_names(show_names):
    for names in show_names:
        print('Greetings ' + ' ' + names.title() + '!')


def modified_names(names, mod_names):
    while names:
        pop_names = names.pop()
        print('Add names: ' + pop_names.title())
        mod_names.append(pop_names)


list_of_names = ['alice', 'bob', 'samanta']

add_names = []

modified_names(list_of_names[:], add_names)


show_complete_modified_names(add_names)

print(list_of_names)
