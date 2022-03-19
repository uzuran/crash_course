# Storing information about pizza being ordered.

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}
# Summarize the order.
print('You ordered a ' + pizza['crust'] + ' crust pizza ' + 'with the following toppings:')

for topping in pizza['toppings']:
    print('\t' + topping)

