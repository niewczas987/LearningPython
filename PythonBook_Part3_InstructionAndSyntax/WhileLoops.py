#przykładowa pętla
x= 'mielonka'
while x:
    print(x, end=' ')
    x = x[1:]

#pass - puste miejsce w kodzie
def func1():
    pass    #tu keidys będize kod funkcji - na razei nie rób nic

#continue - powrót do nagłówka pętli
x=10
while x:
    x=x-1
    if x%2 !=0: continue    #pomijam liczby nieparzyste
    print(x,end = ' ')
print('\n')
#break - wyjscie z petli
while True:
    name = input('Podaj imie:')
    if name =='stop': break
    age = input('Podaj wiek:')
    print('Witaj, ',name,'=>',int(age)**2)

#else - kiedy niespelniony jest warunek while

def liczba_pierwsza(y):
    x = int(y)//2
    while x>1:
        if int(y) % x ==0:
            print(y, 'ma czynnik',x)
            break
        x=-1
    else:
        print(y, 'nie jest liczba pierwsza')
y = input('Podaj liczbe:')
liczba_pierwsza(y)