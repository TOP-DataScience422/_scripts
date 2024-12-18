from pandas import DataFrame

from re import compile


text = '''Pattern.search(string[, pos[, endpos]])
Scan through string looking for the first location where this regular expression produces a match, and return a corresponding Match. Return None if no position in the string matches the pattern; note that this is different from finding a zero-length match at some point in the string.

The optional second parameter pos gives an index in the string where the search is to start; it defaults to 0. This is not completely equivalent to slicing the string; the '^' pattern character matches at the real beginning of the string and at positions just after a newline, but not necessarily at the index where the search is to start.

The optional parameter endpos limits how far the string will be searched; it will be as if the string is endpos characters long, so only the characters from pos to endpos - 1 will be searched for a match. If endpos is less than pos, no match will be found; otherwise, if rx is a compiled regular expression object, rx.search(string, 0, 50) is equivalent to rx.search(string[:50], 0).

>>> pattern = re.compile("d")
>>> pattern.search("dog")     # Match at index 0
<re.Match object; span=(0, 1), match='d'>
>>> pattern.search("dog", 1)  # No match; search doesn't include the "d"'''


pat_funcs = compile(r'((?:\w+?\.)?\w+?\().*?\)')

matches = []
for match in pat_funcs.finditer(text):
    matches.append((*match.span(), f'{match.group(1)})'))

matches = DataFrame(matches, columns=['start', 'end', 'func name'])

# >>> matches
#    start   end         func name
# 0      0    39  Pattern.search()
# 1    982  1006       rx.search()
# 2   1024  1049       rx.search()
# 3   1066  1081      re.compile()
# 4   1086  1107  pattern.search()
# 5   1177  1201  pattern.search()

