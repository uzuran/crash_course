requested_toppings = ['mushrooms', 'extra cheese', 'green peppers']

for requested_topping in requested_toppings:
    print('Adding ' + requested_topping + '.')

print('Finished making your pizza')

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print('Sorry we don`t have any of green peppers')
    else:
        print('Adding ' + requested_topping + '.')
print('Finished making your pizza')

print('\n')

available_toppings = ['mushrooms', 'extra cheese', 'green peppers', 'olives', 'extra pastaPlus']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print('Adding ' + requested_topping + '.')
    else:
        print('Sorry we don`t have french fries, do you wont some olives on your pizza?')

print('Finished your pizza')
