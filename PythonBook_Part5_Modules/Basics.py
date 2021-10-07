#import
import module1
module1.printer('Hello world')
#import from
from module1 import printer
printer('RazDwatrzy')
#skopiowanie wszystkich zmiennych
from module1 import *
printer('www')

from module1 import x,y
x=42
y[0]=44
print(module1.x)
print(module1.y)
import module1
module1.x = 10  #modyfikkacja zmiennex x w innym module
print(module1.x)

from math import sqrt
print(sqrt(144))

import module2
print(module2.sys)
print(module2.name)
print(module2.func)
print(module2.klasa)
print(list(module2.__dict__.keys()))
print(dir(module2))


#przeładowanie modułów
import changer
changer.printer()
from importlib import reload
reload(changer)
changer.printer()
