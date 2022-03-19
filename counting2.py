ask_your_age = 'Tell us how old are you ? \n'
ask_your_age += 'For end enter "quit"\n'

activate = True

while activate:
    message = int(input(ask_your_age))
    if message == 'quit':
        activate = False
    elif message < 3:
        print('You have a free ticket')
        break
    elif message <= 12:
        print('Your ticket price is 10$ ')
        break
    elif message > 12:
        print('Your ticket price is 15$ ')
        break

