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
