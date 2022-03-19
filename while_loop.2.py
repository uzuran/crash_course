prompt = '\nTell me something, and i will repeat it back to you:'
prompt += '\nEnter "quit"  to end the program.'

activate = True

while activate:
    message = input(prompt)
    if message == 'quit':
        activate = False

    else:
        print(message)


