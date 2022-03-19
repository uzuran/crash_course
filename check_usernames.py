current_users = ['sveta', 'artem', 'marharyta', 'marina', 'sara']
new_users = ['lena', 'sveta', 'SVETA', 'michail', 'sergej', 'marina']

for new_user in new_users:
    if new_user.lower() in current_users:
        print(new_user.title() + ' This user name is not available please chose other name  ')
    else:
        print(new_user.title() + ' This name is available !')
