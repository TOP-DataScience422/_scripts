text = 'кот учёный'
text_len = len(text)
print(f'{text!r} {text_len}\n')

pack = zip(
    range(text_len), 
    text, 
    range(-text_len, 0),
)
for i_p, ch, i_n in pack:
    print(f'{i_p} {ch!r} {i_n}')

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

