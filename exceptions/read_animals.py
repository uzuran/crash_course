filenames = ['cats', 'dogs']

try:

    for filename in filenames:
        with open(filename) as file_object:
            content = file_object.read()
            print(content)
except FileNotFoundError:
    pass
