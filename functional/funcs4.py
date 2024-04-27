def point(x, y, /, quarter):
    ...
    print(f'{x=}\t{y=}\t{quarter=}')
    ...


# >>> point(1, 1, 1)
# x=1     y=1     quarter=1
# >>>
# >>> point(1, 1, quarter=4)
# x=1     y=1     quarter=4
# >>>
# >>> point(quarter=2, x=1, y=1)
# TypeError: point() got some positional-only arguments passed as keyword arguments: 'x, y'
# >>>
# >>> point(quarter=2, y=1, x=1)
# TypeError: point() got some positional-only arguments passed as keyword arguments: 'x, y'

