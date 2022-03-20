from collections import OrderedDict

favorite_language = OrderedDict()

favorite_language['artom'] = 'python'
favorite_language['ritochka'] = 'java script'
favorite_language['lukas'] = 'java'
favorite_language['edward'] = 'ruby'

for name, language in favorite_language.items():
    print(f'{name.title()}, favorite language is {language.title()}')
