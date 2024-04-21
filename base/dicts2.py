menu = dict([
    ('борщ', 150), 
    ('солянка', 135), 
    ('том-ям', 180)
])

for key in menu:
    print(f'{key=}')
print()

for value in menu.values():
    print(f'{value=}')
print()

for item in menu.items():
    print(f'{item=}')
print()

for key, value in menu.items():
    print(f'{key=} {value=}')
print()

# >>> menu['борщ']
# 150
# >>> menu['том-ям']
# 180
# >>> menu['солянка']
# 135

# >>> menu['том-ям'] = 190
# >>> menu
# {'борщ': 150, 'солянка': 135, 'том-ям': 190}

# >>> menu.get('солянка')
# 135
# >>> menu.get('солянка', 0)
# 135
# >>> menu.get('ростбиф')
# >>>
# >>> menu.get('ростбиф', 0)
# 0

