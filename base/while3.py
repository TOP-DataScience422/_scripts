text = 'кот учёный'
text_len = len(text)
print(f'{text!r} {text_len}\n')

i_p = 0
i_n = -text_len
while i < text_len:
    print(f'{i_p} {text[i_n]!r} {i_n}')
    i_p += 1
    i_n += 1

# 'кот учёный' 10
# 
# 0 'к' -10
# 1 'о' -9
# 2 'т' -8
# 3 ' ' -7
# 4 'у' -6
# 5 'ч' -5
# 6 'ё' -4
# 7 'н' -3
# 8 'ы' -2
# 9 'й' -1

# >>> text[-1]
# 'й'
# >>> text[len(text)-1]
# 'й'

# >>> text[-15]
# IndexError: string index out of range

