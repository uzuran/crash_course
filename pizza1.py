def make_pizza(size, *toppings):
    print('\nMaking a ' + str(size) + '-ich pizza with followings toppings: ')
    for topping in toppings:
        print(f'-{topping}')


make_pizza(16, 'pepperoni')
make_pizza(20, 'mushrooms', 'cheese', 'green pepperoni')

