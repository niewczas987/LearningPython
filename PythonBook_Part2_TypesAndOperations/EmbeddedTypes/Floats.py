# LICZBY ZMIENNOPRZECINKOWE - FLOATS
print(1 / 3)
print((2 / 3) + (1 / 2))
import decimal

d = decimal.Decimal('3.141')
print(d + 1)
decimal.getcontext().prec = 2
print(decimal.Decimal(1.00)/decimal.Decimal(3.00))
#ulamki
from fractions import Fraction
f = Fraction(2,3)
print(f+1)