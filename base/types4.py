print(f'{str(10) = }')
print(f'{repr(10) = }\n')

print(f'{str(.1) = }')
print(f'{repr(.1) = }\n')

print(f'{str(1+1j) = }')
print(f'{repr(1+1j) = }\n')

from decimal import Decimal as dec
from fractions import Fraction as frac

print(f'{str(dec("0.95")) = }')
print(f'{repr(dec("0.95")) = }\n')

print(f'{dec("0.95")}')
print(f'{dec("0.95")!s}')
print(f'{dec("0.95") = !s}')
print(f'{dec("0.95") = }')
print(f'{dec("0.95") = !r}\n')

print(f'{str(frac(1, 5)) = }')
print(f'{repr(frac(1, 5)) = }\n')

print(f'{str("Abc") = }')
print(f'{repr("Abc") = }\n')

print(f'{str([1, 2, 3]) = }')
print(f'{repr([1, 2, 3]) = }\n')

class UserType:
    pass

obj = UserType()
print(f'{str(obj) = }')
print(f'{repr(obj) = }\n')

