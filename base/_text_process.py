poem = '''У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.'''

punctuation = '.,:;!?-—…'

# остаются пустые строки после удаления тире
words = [
    word.rstrip(punctuation).lower()
    for word in poem.split()
]

# обрабатываем и включаем в список слов только те строки, в которых есть хотя бы одна буква
words = []
for word in poem.split():
    for ch in word:
        if ch.isalpha():
            break
    else:
        continue
    words.append(word.rstrip(punctuation).lower())

# минимальное количество итераций
words = []
stripping = True
for word in poem.split():
    word_clean = ''
    for ch in word[::-1]:
        if stripping and ch in punctuation:
            continue
        else:
            stripping = False
        word_clean = ch.lower() + word_clean
    if word_clean:
        words.append(word_clean)
    stripping = True

