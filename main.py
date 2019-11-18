#case4
"""Case-study #3 Анализ текста
Developers: Revtova L.
            Arkhipova A.

"""
import textblob as tb
print('Выберите на каком языке вводится текст и введите число:')
print('1 - Русский\n'
      '2 - English')
choise = int(input())
if choise == 1:
    text = input("Введите текст:")
    text = text.lower()

    sentences = text.count('.')
    words = text.count(' ') + 1
    syllables = text.count('ё') + text.count('у') + text.count('е') + text.count('ы') + text.count('а') + text.count('о') + text.count('э') + text.count('я') + text.count('и') + text.count('ю')
    avrg_stns_len = words / sentences
    avrg_wrd = syllables / words
    index = 206.835 - (1.3 * avrg_stns_len) - (60.1 * avrg_wrd)


    print('Предложений:', sentences)
    print('Слов:', words)
    print('Слогов:', syllables)
    print('Средняя длина предложения в словах:', avrg_stns_len)
    print('Средняя длина слова в слогах:', avrg_wrd)
    print('Индекс удобочитаемости Флеша:', index)

    if index > 80:
        print('Текст очень легко читается (для младших школьников).')
    elif index > 50:
        print('Простой текст (для школьников).')
    elif index > 25:
        print('Текст немного трудно читать (для студентов).')
    else:
        print('Текст трудно читается (для выпускников ВУЗов).')
elif choise == 2:
    text = input("Введите текст:")
    text = text.lower()

    sentences = text.count('.')
    words = text.count(' ') + 1
    syllables = text.count('e') + text.count('y') + text.count('u') + text.count('i') + text.count('o') + text.count(
        'a')
    avrg_stns_len = words / sentences
    avrg_wrd = syllables / words
    index = 206.835 - 1.015 * avrg_stns_len - 84.6 * avrg_wrd

    print('Предложений:', sentences)
    print('Слов:', words)
    print('Слогов:', syllables)
    print('Средняя длина предложения в словах:', avrg_stns_len)
    print('Средняя длина слова в слогах:', avrg_wrd)
    print('Индекс удобочитаемости Флеша:', index)

    if abs(index) > 65:
        print('Простой английский текст.')
    elif abs(index) > 30:
        print('Немного трудно читать.')
    else:
        print('Очень трудно читать.')

    testimonial = tb.TextBlob(text)
    print('Объективность: ', end='')
    print(format(testimonial.sentiment.polarity * 100, '.1f') + '%')