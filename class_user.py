class User:
    def __init__(self, user_name, email_address, country):
        self.name = user_name
        self.email = email_address
        self.country = country

    def describe_user(self):
        print('Name: ' + self.name + '\n' + 'Email address: ' + self.email + '\n' + 'Country: ' + self.country)

    def greetings(self):
        print('Hello! ' + self.name + ' how are you ?' + '\n')


class Admin(User):
    def __init__(self, user_name, email_address, country):
        super(Admin, self).__init__(user_name, email_address, country)
        self.privileges = Privileges([])

class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges


    def show_privileges(self):
        for privilege in self.privileges:
            print('-' + privilege)

admin = Admin('Admin', 'admin@gmail.com', 'Czech')

admin.describe_user()

admin_privilege = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]
admin.privileges.privileges = admin_privilege
admin.privileges.show_privileges()


print('\n')


user1 = User('Artom', 'artom.plzen@gmail.com', 'Belarus')

user1.describe_user()
user1.greetings()

user2 = User('Ritochka', 'mpsu@gmail.com', 'Ukraine')


user2.describe_user()
user2.greetings()
