def gobad(x,y):
    return x/y

def gosouth(x):
    print(gobad(x,0))

# gosouth(1)

def kaboom(x,y):
    return x+y

try:
    kaboom([0,1,2],'mielonka')
except TypeError:
    print('Zgłoszono Type Error')
print('wznowienie programu')

class MyError(Exception):
    pass

def stuff(file):
    raise MyError()

file = open('data','w')
try:
    stuff(file)
finally:
    file.close()
print('program nie doszedł tutaj')