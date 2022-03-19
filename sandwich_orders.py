sandwich_order = ['Egg Sandwich', 'Seafood Sandwich', 'Roast Beef Sandwich', 'pastrami', 'Grilled Cheese', 'pastrami',
                  'pastrami']
finished_sandwiches = []

while 'pastrami' in sandwich_order:
    sandwich_order.remove('pastrami')

while sandwich_order:
    sandwiches_we_have = sandwich_order.pop()
    print('Sandwiches we have: ' + sandwiches_we_have)
    finished_sandwiches.append(sandwiches_we_have)

print('\n')

for finished_sandwich in finished_sandwiches:
    print('I make fot you ' + finished_sandwich)
