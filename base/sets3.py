text = '''A dictionary’s keys are almost arbitrary values. Values that are not hashable, that is, values containing lists, dictionaries or other mutable types (that are compared by value rather than by object identity) may not be used as keys. Values that compare equal (such as 1, 1.0, and True) can be used interchangeably to index the same dictionary entry.'''

unique_chars = set(text)

# >>> len(text)
# 350
# >>> len(unique_chars)
# 34

# >>> unique_chars
# {'v', ')', 'c', 'n', ',', 'h', 'A', 'b', 'q', 'V', 't', 's', 'g', 'k', '.', '0', 'r', 'j', ' ', 'd', 'i', 'y', 'p', '(', 'm', 'u', 'x', 'T', '1', 'l', '’', 'a', 'e', 'o'}

# >>> set(text.lower())
# {'v', ')', 'c', 'n', ',', 'h', 'b', 'q', 't', 's', 'g', 'k', '.', '0', 'r', 'j', ' ', 'd', 'i', 'y', 'p', '(', 'm', 'u', 'x', '1', 'l', '’', 'a', 'e', 'o'}
# >>>
# >>> len(set(text.lower()))
# 31
