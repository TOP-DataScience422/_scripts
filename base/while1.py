# while <проверочное_выражение_продолжения_цикла>:
#     <тело_цикла>
#     ...

prompt = '\n _> '
command = input(prompt)
# условие продолжения цикла
while command != 'exit':
    if command == 'line':
        print('—'*40)
    command = input(prompt)

print('\n')

while True:
    command = input(prompt)
    if command == 'line':
        print('—'*40)
    # условие прерывания цикла
    elif command == 'exit':
        break

