sep = '-' *32 + '\n'

print(sep + 'Wyjątek zgłoszony i przechwycony')
try:
    x='spam'[99]
except IndexError:
    print('Wykonano except')
finally:
    print('Wykonano finally')
print('Po wykonaniu')

print(sep + 'Wyjątek nie został zgłoszony')
try:
    x='spam'[3]
except IndexError:
    print('Wykonano except')
finally:
    print('Wykonano finally')
print('Po wykonaniu')

print(sep + 'Wyjątek nie zgłoszony, wykonano else')
try:
    x='spam'[99]
except IndexError:
    print('Wykonano except')
else:
    print('Wykonano else')
finally:
    print('Wykonano finally')
print('Po wykonaniu')

print(sep + 'Wyjątek zgłoszony, ale nie przechwycony')
try:
    #x=1/0 #nie obsłużony wyjątek, bo obsłużone tylko IndexError
    x=5
except IndexError:
    print('Wykonano except')
finally:
    print('Wykonano finally')
print('Po wykonaniu')

#przechwytywanie wyjątków z użyciem raise
# try:
#     raise IndexError('mielonka')
# except IndexError:
#     print('przekazywanie')
#     raise


