f= open('TestsInstructions.py')
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print('='*20)

#to samo z instrukcją __next__
f = open('Expressions.py')
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())

print('='*20)
for line in open('TestsInstructions.py'):
    print(line.upper(),end=' ')
#wczytanie pliku używając 'while'
print('='*20)
f = open('Expressions.py')
while True:
    line = f.readline()
    if not line: break
    print(line.upper())


#kontrola iteracji - 'iter i 'next'
print('='*20)
L=[1,2,3,4,5]
I = iter(L)
print(I.__next__())
print(I.__next__())
print(I.__next__())
print(I.__next__())

#sprawdzenie, czy obiekt jest iterowany
f=open('Expressions.py')
if iter(f) is f:
    print('Obiekt iterowany')
else:
    print('Obiekt nieiterowany')

L=[1,2,3]
I = iter(L)
while True: #przykład ręcznej iteracji
    try:
        X=next(I)
    except StopIteration:
        break
    print(X**2, end=' ')

#inne iteratory typów wbudowanych
D={'a':1,'b':2,'c':3}
I = iter(D)
print(I.__next__())
print(I.__next__())

#iterowanie po range
print('Iterowanie po range')
R=range(5)
I=iter(R)
print(I.__next__())
print(I.__next__())
#iterowanie po enumerate
print('Iterowanie po enumerate')
E = enumerate('spam')
I = iter(E)
print(I.__next__())
print(I.__next__())
