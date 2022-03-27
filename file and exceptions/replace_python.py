file = 'learning_python'

with open(file) as file_object:
    lines = file_object.readlines()

print(lines)
print('\n')


for line in lines:
    liine = line.rstrip()
    print(liine.replace('Python', 'C'))

for line in lines:
    print(line) 


