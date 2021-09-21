#first script
import sys

import myfile

print(sys.platform) #kom1
print(2**100) #kom2
x='xD' #string
print (x*3) #powtorzenie lancucha znakow
print(myfile.title)

from myfile import title
print("Zaimportowany title instrukcją 'import' : "+ title)

#input()