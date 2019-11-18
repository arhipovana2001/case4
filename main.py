"""Case-study #3 Анализ текста
Developers: Revtova L.
            Arkhipova A.

"""

import local
choose = int(input((local.CHOOSE)))
if choose == 1:
    import local_english as lc
elif choose == 2:
    import local_russian as lc
elif choose == 3:
    import local_italian as lc

import textblob as tb
print(lc.TEXT_BLOB)
print(lc.LANGUAGE_1)
print(lc.LANGUAGE_2)
choise = int(input())
if choise == 1:

    text = input(lc.TEXT)
    text = text.lower()

    sentences = text.count('.')
    words = text.count(' ') + 1
    vowels = lc.VOWELS
    syllables = 0
    for i in text:
        if i in vowels:
            syllables += 1
    avrg_stns_len = words / sentences
    avrg_wrd = syllables / words
    index = 206.835 - (1.3 * avrg_stns_len) - (60.1 * avrg_wrd)

    print(lc.SENTENCES, sentences)
    print(lc.WORD, words)
    print(lc.SYLLABLES, syllables)
    print(lc.AVERAGE_SENTENCES, avrg_stns_len)
    print(lc.AVERAGE_WORD, avrg_wrd)
    print(lc.INDEX_FLESH, index)

    if index > 80:
        print(lc.TEXT_EASY)
    elif index > 50:
        print(lc.TEXT_SIMPLE)
    elif index > 25:
        print(lc.TEXT_LITTLE_HARD)
    else:
        print(lc.TEXT_DIFFICULT)

elif choise == 2:
    text = input(lc.TEXT)
    text = text.lower()

    sentences = text.count('.')
    words = text.count(' ') + 1
    vowels = lc.VOWELS
    syllables = 0

    for i in text:
        if i in vowels:
            syllables += 1
    avrg_stns_len = words / sentences
    avrg_wrd = syllables / words
    index = 206.835 - (1.3 * avrg_stns_len) - (60.1 * avrg_wrd)

    print(lc.SENTENCES, sentences)
    print(lc.WORD, words)
    print(lc.SYLLABLES, syllables)
    print(lc.AVERAGE_SENTENCES, avrg_stns_len)
    print(lc.AVERAGE_WORD, avrg_wrd)
    print(lc.INDEX_FLESH, index)

    if abs(index) > 65:
        print(lc.ENGLISH_SIMPLE)
    elif abs(index) > 30:
        print(lc.DIFFICULT)
    else:
        print(lc.VERY_HARD)

    testimonial = tb.TextBlob(text)
    tonality = testimonial.sentiment.polarity * 100
    objectivity = (1 - testimonial.sentiment.subjectivity) * 100
    print(tonality)
    print('Объективность:', format(objectivity, '.1f') + '%')
