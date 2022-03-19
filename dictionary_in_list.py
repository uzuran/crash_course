a_dictionary = {"name": "John", "age": 20}
a_list = []
dictionary_copy = a_dictionary.copy()
a_list.append(dictionary_copy)

for name, age in dictionary_copy.items():
    print(name + ' ' + str(age))
print('\n')

# Pets and their owners

dog = {
    'color': 'black',
    'weight': 30,
    'race': 'doga'

}

cat = {
    'color': 'white',
    'weight': 6,
    'race': 'pers'

}

dog_list = [dog]
cat_list = [cat]

print('Dog: ')
for info1 in dog_list:
    for i, x in info1.items():
        print(i + ' ' + str(x))

print('\n')

print('Cat: ')
for info1 in cat_list:
    for i, x in info1.items():
        print(i + ' ' + str(x))
