def greet_users(names):
    for name in names:
        msg = 'Hello, ' + name.title() + '!'
        print(msg)


username = ['hana', 'jirka', 'anatoly']

greet_users(username)
