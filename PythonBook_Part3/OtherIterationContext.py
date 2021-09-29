print('uppers')
uppers = [line.upper() for line in open('Expressions.py')]
print(uppers)
#używając map
print('map')
print(list(map(str.upper, open('Expressions.py'))))
#instrukcja sorted
print('sorted')
print(sorted(open('Expressions.py')))
#instrukcja zip
print('zip')
print(list(zip(open('Expressions.py'),open('Expressions.py'))))
#instrukcja enumerate
print('enumerate')
print(list(enumerate(open('Expressions.py'))))
#instrukcja bool
print('bool')
print(list(filter(bool,open('Expressions.py')))) #wypisanie niepustych wierszy
#funkcja reduce
print('funkcja reduce')
import functools,operator
print(functools.reduce(operator.add, open('Expressions.py')))
#ine funkcje wbudowane
print('-'*20)
print(sum([1,3,4,5,6])) #19
print(any(['spam','','ni']))    #True
print(all(['spam','','ni']))    #False
print(max([1,3,4,5,6]))         #6
print(min([1,3,4,5,6]))         #1

#kontekst teracyjny *arg
def f(a,b,c,d):
    print(a,b,c,d,sep='&')

f(1,2,3,4)
f(*[1,2,3,4])
#f(*open('Expressions.py')) - daje błąd, bo za dużo argumentów - każda linia staje sie argumentem