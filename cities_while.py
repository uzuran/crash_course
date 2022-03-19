prompt = '\nPlease enter the name of city you have visited:'

prompt += '\nEnter "quit" when you are finished.\n'

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print('I"d love to go to ' + city.title() + '!')
