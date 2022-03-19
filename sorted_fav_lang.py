favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
new_users = ['alice', 'samanta', 'kolek', 'phil', 'edward']

for new_user in new_users:
    if new_user in favorite_languages:
        print('Thank you for responding ' + new_user.title())
    else:
        print('Hello do you wont take a poll? ' + new_user.title())

print('\n')
for name in sorted(favorite_languages.keys()):
    print(name.title() + ', thank you for taking pool')

print('\nThe following language are mentioned\n')       # cz nasledujici jazyky jsou zmineny
for language in favorite_languages.values():
    print(language.title())

print('\nEliminated tow time python\n')
# use set for eliminate double time writing the same word

print('The following language are mentioned')       # cz nasledujici jazyky jsou zmineny
for language in set(favorite_languages.values()):
    print(language.title())

