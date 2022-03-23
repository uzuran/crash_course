file = 'pi_digits.txt'

with open(file) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(lines)
print(pi_string)
print(len(pi_string))
