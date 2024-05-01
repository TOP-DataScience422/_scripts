def map_simple(func_obj: 'function', iterator: 'iterable') -> list['any']:
    result = []
    for elem in iterator:
        result.append(func_obj(elem))
    return result


def char_to_byte(char: str) -> bytes:
    return bytes(hex(ord(char)), encoding='utf-8')


# >>> map_simple(char_to_byte, 'Python - лучший!')
# [b'0x50', b'0x79', b'0x74', b'0x68', b'0x6f', b'0x6e', b'0x20', b'0x2d', b'0x20', b'0x43b', b'0x443', b'0x447', b'0x448', b'0x438', b'0x439', b'0x21']
# >>>
# >>> b''.join(map_simple(char_to_byte, 'Python - лучший!'))
# b'0x500x790x740x680x6f0x6e0x200x2d0x200x43b0x4430x4470x4480x4380x4390x21'


text = '''If one positional argument is provided, it should be an iterable. The largest item in the iterable is returned. If two or more positional arguments are provided, the largest of the positional arguments is returned.'''

# >>> map_simple(
# ...     lambda s: (len(s), s),
# ...     text.split()
# ... )
# [(2, 'If'), (3, 'one'), (10, 'positional'), (8, 'argument'), (2, 'is'), (9, 'provided,'), (2, 'it'), (6, 'should'), (2, 'be'), (2, 'an'), (9, 'iterable.'), (3, 'The'), (7, 'largest'), (4, 'item'), (2, 'in'), (3, 'the'), (8, 'iterable'), (2, 'is'), (9, 'returned.'), (2, 'If'), (3, 'two'), (2, 'or'), (4, 'more'), (10, 'positional'), (9, 'arguments'), (3, 'are'), (9, 'provided,'), (3, 'the'), (7, 'largest'), (2, 'of'), (3, 'the'), (10, 'positional'), (9, 'arguments'), (2, 'is'), (9, 'returned.')]

