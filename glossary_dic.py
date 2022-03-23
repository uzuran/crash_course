from collections import OrderedDict

glossary = OrderedDict()

glossary['append'] = ' add item in list at the end position'
glossary['isupper'] = ' make string charter Up case'
glossary['islower'] = ' make all str charter lowercase'
glossary['set'] = ' eliminate same words on value or keys'

for method, gloss in glossary.items():
    print(f'{method}:{gloss}')
