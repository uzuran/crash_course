file = 'stories_for_boys'

with open(file) as file_object:
    content = file_object.read()
    count = content.lower().count('the')
    print(f'The count of the word is {count}')
