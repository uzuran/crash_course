names = ['admin', 'artem', 'marharyta', 'bob', 'sara']
names.clear()
if len(names) == 0:
    print('List is empty')
for name in names:
    if name == 'admin':
        print('Hello ' + name.title() + ', ' + 'would you like to see a status report?')
    else:
        print('Hello ' + name.title() + ', ' + 'thank you for loging again')
