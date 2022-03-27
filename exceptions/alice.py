def count_words(filenames):
    try:
        with open(filenames) as f_obj:
            content = f_obj.read()
    except FileNotFoundError:
        print(f'Sorry {filenames} does not exist.')

    else:
        words = content.split()
        num_words = len(words)
        print(f'The {filenames} has about {num_words} words.')


filenames = ['alice_in_wonderland', 'stories_for_boys', 'this file dose not exist']
for filename in filenames:
    count_words(filename)
