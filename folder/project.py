# import webbrowser
# t = input('введите текст для перевода ')
# url = 'https://translate.google.com/?sl=auto&tl=en&text=' + t
# webbrowser.open(url)

from deep_translator import GoogleTranslator
t = input('Введите текст ')
tr = GoogleTranslator(source='ru', target='en').translate(t)
print('перевод',tr)
