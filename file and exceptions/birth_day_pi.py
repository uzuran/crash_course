file = 'billion_of_pi'

with open(file) as file_object:
    lines = file_object.readlines()

    pi_string = ''
    for line in lines:
        pi_string += line.rstrip()

birthday = input('Enter your birthday, in the form mmddyy:')
if birthday in pi_string:
    print('Your birthday is appears in first million digits of pi.')

else:
    print("Your birthday does not appear in the first million digits of pi.")
print(pi_string)
