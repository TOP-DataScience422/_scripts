# for <переменная_цикла> in <выражение_возвращающее_итератор>:
#     <тело_цикла>
#     ...

text = 'python — самый классный!'
print(type(text), text, len(text))

for char in text:
    if char.isalpha():
        char_group = 'буква'
    elif char.isspace():
        char_group = 'пробел'
    elif char in '.,:;!?-–—':
        char_group = 'знак препинания'
    else:
        char_group = 'прочий'
    print(type(char), char, len(char), char_group)

