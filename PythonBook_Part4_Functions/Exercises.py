# Ex.1 - basics
print('Ex1'+'='*30)
def Ex1(var):
    print(var)
Ex1('TestTest')
Ex1(123)
Ex1([1,2,3,4])
Ex1({'a':1,'b':2,'c':3})
#Ex1() ->TypeError: Ex1() missing 1 required positional argument: 'var'

#Ex2
print('Ex2'+'='*30)
def adder(var1,var2):
    return var1+var2
print(adder('abc','cde'))
print(adder(100,200))
print(adder([1,2,3],['a','b','c']))
print(adder(2.5,3.5))

#Ex3
print('Ex3'+'='*30)
def adder2(*args):
    sum = args[0]
    for next in args[1:]:
        sum+= next
    return sum
print(adder2('abc','cde','www','xxx','DDD'))
print(adder2(100,200,400))
print(adder2([1,2,3],['a','b','c'],['g','h']))
print(adder2(2.5,3.5,11))

#Ex4
print('Ex4'+'='*30)
def adder2(*args):
    sum = args[0]
    for next in args[1:]:
        sum+= next
    return sum
print(adder2('abc','cde','www','xxx','DDD'))
print(adder2(100,200,400))
print(adder2([1,2,3],['a','b','c'],['g','h']))
print(adder2(2.5,3.5,11))

#Ex5
print('Ex5'+'='*30)
def adder3(good = 1, bad=2, ugly = 3):
    return good + bad + ugly
print(adder3('abc','cde','www'))
print(adder3(100,200))
print(adder3([1,2,3],['a','b','c'],ugly = ['xD']))
print(adder3())
#adder with dictionary
def adder31(**args):
    keyargs = list(dict.keys(args))
    result = args[keyargs[0]]
    for var in keyargs[1:]:
        result += args[var]
    return result

print(adder31(a=1,b=2,c=3)) #=6
print(adder31(a='aa',b='bb',c='cc'))    #funkcja przyjmuje jako argumenty wartości słownika

#Ex6
print('Ex6'+'='*30)
def copyDict(old ={}):
    new = {}
    for key in old.keys():
        new[key]=old[key]
    return new
def addDict(d1,d2):
    new = {}
    for key in d1.keys():
        new[key] = d1[key]
    for key in d2.keys():
        new[key] = d2[key]
    return new

x={1:1}
y={2:2}
z=addDict(x,y)

#Ex7
print('Ex7'+'='*30)
def f1(a,b): print(a,b)
def f2(a,*b):print(a,b)
def f3(a,**b):print(a,b)
def f4(a,*b,**c):print(a,b,c)
def f5(a,b=2,c=3):print(a,b,c)
def f6(a,b=2,*c):print(a,b,c)

f1(1,2)
f1(b=2,a=1)
f2(1,2,3)
f3(1,x=2,y=3)
f4(1,2,3,x=2,y=3)
f5(1)
f5(1,4)
f6(1)
f6(1,3,4)

#Ex8
print('Ex8'+'='*30)
#Przerobić kod na funkcję
# x=y//2
# while x>1:
#     if y%x==0:
#         print((y,'dzieli się przez',x))
#         break
#         x-=1
#     else:
#         print(y,'nie jest liczba pierwszą')

def primeNumbers(number):
    if number <=1: print(number,'nie jest liczbą pierwszą.')
    else:
        x=number//2
        for x in range(int(number),1,-1):
            if number%x==0:
                print(number,'ma czynnik',x)
                break
            x-=1
        else:
            print(number,'nie jest liczbą pierwszą.')
primeNumbers(13)
primeNumbers(15.0)
primeNumbers(3)
primeNumbers(-2)

#Ex9
print('Ex9'+'='*30)
list=[2,4,9,16,25]
import math
def squareRoot(list):
    print(list)
    return ([math.sqrt(x) for x in list])
print(squareRoot(list))




