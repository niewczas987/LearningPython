import PythonBook_Part1_Introduction.module1

from PythonBook_Part4_Functions.BasicsOfFunctions import zliczanieLiteryI
zliczanieLiteryI('iiiiii')
zliczanieLiteryI('kasdnasnasfdasfiasofhioasfo')

print('='*35)
import dir1.dir2.mod
from importlib import reload
reload(dir1)
reload(dir1.dir2)

print(dir1.x)
print(dir1.dir2.y)
print(dir1.dir2.mod.z)

#relative import
import string
print(string)
#from . import string   ->ImportError: attempted relative import with no known parent package
#print(string)