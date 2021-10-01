#funkcje rekurencyjne
def mysum(L):
    if not L:
        return 0
    else:
        return L[0]+mysum(L[1:])

print(mysum([1,2,3,4,5,6]))

#implementacje alternatywne
def mysum1(L):
    return 0 if not L else L[0]+mysum1(L[1:])    #użycie wyrażeń trójskładnikowych
def mysum2(L):
    return L[0] if len(L)==1 else L[0] + mysum2(L[1:])   #dowolny typ, domyslnie wartosc 1
def mysum3(L):
    first,*rest = L
    return first if not rest else first+mysum3(rest)

#obsługa dowolnych struktur przez rekurencję
L=[1,[2,[3,4],5],6,[7,8]]
def sumtree(L):
    tot = 0
    for x in L:
        if not isinstance(x,list):
            tot +=x
        else:
            tot+= sumtree(x)
    return tot

print(sumtree(L))

#wyrażenia LAMBDA
f = lambda x,y,z: x+y+z
print(f(1,2,3))
x= (lambda a='raz',b='dwa',c='trzy':a+b+c)
print(x())
print(x('las'))
L=[(lambda x: x**2),(lambda x:x**3),(lambda x: x**4)]   #tablica skoków - przykładowe zastosowanie
for f in L:
    print(f(2))
#wyrażenia trójargumentowe w lambda
lower = (lambda x,y: x if x<y else y)
#użycie map
import sys
showall = (lambda x: map(sys.stdout.write, x))


#odwzorowanie funkcji na sekwencje - MAP
counters = [1,2,3,4]
def inc(x): return x+10
print(list(map(inc, counters)))
print(list(map((lambda x: x+5), counters)))
print(list(map(pow,[1,2,3],[2,3,4])))   #użycie z potęgowaniem ->[1, 8, 81]

#programowanie funkcyjne - FILTER i REDUCE
print(list(filter((lambda x:x>0), range(-5,5))))
from functools import reduce
print(reduce((lambda x,y: x+y),[1,2,3,4]))