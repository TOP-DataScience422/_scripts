def filter_simple(predicate: 'function', iterator: 'iterable') -> list:
    result = []
    for elem in iterator:
        if predicate(elem):
            result.append(elem)
    return result


char_digits = set('0123456789')
first_char =  char_digits | {'-'}

def is_intable(number: str) -> bool:
    try:
        first = set(number[0]) <= first_char
    except IndexError:
        return False
    else:
        return first and set(number[1:]) <= char_digits


# filter_simple(is_intable, ['10-24', '-15', '2', '2 2', '14'])
# ['-15', '2', '14']


text = '''If one positional argument is provided, it should be an iterable. The largest item in the iterable is returned. If two or more positional arguments are provided, the largest of the positional arguments is returned.'''

# >>> filter_simple(
# ...     lambda w: len(w) > 3, 
# ...     text.split()
# ... )
# ['positional', 'argument', 'provided,', 'should', 'iterable.', 'largest', 'item', 'iterable', 'returned.', 'more', 'positional', 'arguments', 'provided,', 'largest', 'positional', 'arguments', 'returned.']

