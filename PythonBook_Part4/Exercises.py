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
print(adder2('abc','cde'))
print(adder2(100,200))
print(adder2([1,2,3],['a','b','c']))
print(adder2(2.5,3.5))
print(adder2())
#Ex4
print('Ex4'+'='*30)

#Ex5
print('Ex5'+'='*30)

#Ex6
print('Ex6'+'='*30)

#Ex7
print('Ex7'+'='*30)

#Ex8
print('Ex8'+'='*30)

#Ex9
print('Ex9'+'='*30)

#Ex10
print('Ex10'+'='*30)



