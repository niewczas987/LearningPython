def min1(*args):
    res = args[0]
    for arg in args[1:]:
        if arg < res:
            res= arg
    return res

def min2(first, *rest):
    for arg in rest:
        if arg < first:
            first =arg
    return first

def min3(*args):
    tmp =list(args)
    tmp.sort()
    return tmp[0]

print(min1(4,5,6,3))
print(min2('bb','aa','cc'))
print(min3([2,2],[1,1],[4,4]))


#przykładowa funkcJA działająca i na min i na max
def minmax(test,*args):
    res = args[0]
    for arg in args[1:]:
        if test(arg, res):
            res = arg
    return res

def lessthan(x,y):return x<y
def greaterthan(x,y): return x>y

print(minmax(lessthan,4,2,6,7,8,1)) #minimum
print(minmax(greaterthan,4,2,6,7,8,1)) #maximum