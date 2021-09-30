# pierwszy przykad
def times(x, y):  # utworzenie i przypisanie funkcji
    return x * y  # ciało funkcji wykonywane po wywołaniu


print(times(3, 8))  # wwołanie funkcji z argumentami
print(times('xD', 10))  # argumenty mogą być dowolne, bo polimorfizm przy *


def intersect(seq1, seq2):
    res=[]
    for x in seq1:
        if x in seq2:
            res.append(x)
    print(res)

s1 = 'mielonka'
s2 = 'biedronka'
intersect(s1,s2)

def zliczanieLiteryI(x):
    result = 0
    for c in x:
        if c == 'i':
            result = result+1
    if result==1:
        print('W słowie {} jest {} litera \'i\''.format(x,result))
    elif result in range(2,5):
        print('W słowie', x, 'jest', str(result), 'litery \'i\'')
    else:
        print('W słowie', x, 'jest', str(result), 'liter \'i\'')

zliczanieLiteryI('Eliza')
zliczanieLiteryI('Eliiza')
zliczanieLiteryI('Eliiiiiza')