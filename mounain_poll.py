responses = {}

# Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
    # Prompt for the person`s name and response.
    name = input('What is your name?\n')
    response = input('Which mountain  would you like climb someday \n')

    # Store response in the dictionary:
    responses[name] = response
    # Find out if anyone else is going to take the poll.
    repeat = input('Would you like to let another person respond ? (yes/no)')
    if repeat == 'no':
        polling_active = False

# Polling is complete.Show the results
print('\n---Polls Results---')
for name, response in responses.items():
    print(name + ' would like to climb ' + response + '.')

