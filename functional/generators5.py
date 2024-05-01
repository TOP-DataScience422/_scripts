# <объект_генератор> = (
#     <выражение_для_элемента>
#     for <переменная_цикла> in <выражение_возвращающее_итератор>
#     if <условие_вычисления_выражения_для_элемента>
# )

numbers = (int(n) for n in input(' > ').split())
#  > 1 2 3 5 6 7 9 10 11
# >>>
# >>> numbers
# <generator object <genexpr> at 0x000001A0A17FC520>


words = (w.lower() for w in input(' > ').split())
#  > в начале было слово
# >>>
# >>> words
# <generator object <genexpr> at 0x000001A0A17FE330>

