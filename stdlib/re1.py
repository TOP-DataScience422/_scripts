from re import compile as re_compile

text = '''При первом способе написания следует придерживаться следующих догм:

цифры в дате — только арабские (напомним: 1, 2, 3...),
парное написание и для числа, и для месяца,
каждое обозначение отделяется от предыдущего точкой (06.06), пробелы не нужны,
последовательность написания даты чаще всего такова: число, месяц, год (06.06.1799), допускается и обратная (1799.06.06), но используется она для удобства при составлении каталогов, архивов и прочего,
если дата записывается цифрами, то сокращение «г.» или слово «год» не нужны: 06.06.1799.
Словесно-цифровой способ не намного сложнее, выглядит он так:

6 июня 1799 года или 6 июня 1799 г.,
если месяц и число не указаны, то слово «год» пишется полностью: 1799 год, НО: в июне 1799 г., во втором полугодии 1799 г., за 2 месяца 1799 года,
слово «год» не пишется, например, при оформлении обложек и титульных листов (1799),
для обозначения кварталов используются римские цифры (II квартал 2000 г.), при ограничении определенного периода верным будет: 1799–1837 гг., через короткое тире, но без пробелов,
принятое сокращение для обозначения нескольких лет или временного промежутка, ограниченного годами: « гг.»; через пробел от числового значения,
не календарные годы или сезоны (учебный, отчетный) пишутся через «слэш»: в 2000/2001 году.'''

pat_date = re_compile(r'(?P<day>0[1-9]|[12]\d|3[01])\.'
                      r'(?P<month>0[1-9]|1[012])\.'
                      r'(?P<year>\d{4})')

dates_list = pat_date.findall(text)

# >>> dates_list
# [('06', '06', '1799'), ('06', '06', '1799')]

dates_mo = pat_date.finditer(text)

# >>> dates_mo
# <callable_iterator object at 0x000001272B686A70>
# >>>
# >>> for mo in dates_mo:
# ...     print(mo['year'], mo['month'], mo['day'])
# ...
# 1799 06 06
# 1799 06 06

