curent_number = 1
while curent_number <= 5:
    print(curent_number)
    curent_number += 1


prompt = '\nTell me something, and i will repeat it back to you:'
prompt += '\nEnter "quit"  to end the program.'

message = ''
while message != 'quit':
    message = input(prompt)
    print(message)
