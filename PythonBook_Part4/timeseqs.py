#sprawdzanie wydajnosci poszczególnych implementacji
import sys, mytimer
reps = 10000
repslist = range(reps)

def forLoop():
    res = []
    for x in repslist:
        res.append(x+10)
    return res

def listComp():
    return [x+10 for x in repslist]

def mapCall():
    return list(map(lambda x:x+10,repslist))

def genExpr():
    return list(x+10 for x in repslist)

def genFunc():
    def gen():
        for x in repslist:
            yield x+10
    return list(gen())

print(sys.version)
for test in (forLoop,listComp,mapCall,genExpr,genFunc):
    elapsed, result = mytimer.timer(test)
    print('-'*33)
    print('%-9s: %.5f => [%s..%s]'%(test.__name__,elapsed,result[0],result[-1]))

#wyniki dla funkcji 'abs'
# forLoop  : 0.72058 => [0..9999]
# listComp : 1.19508 => [0..9999]
# mapCall  : 1.43359 => [0..9999]
# genExpr  : 1.98624 => [0..9999]
# genFunc  : 2.53744 => [0..9999]

#wyniki dla 'x+10'
# forLoop  : 0.76559 => [10..10009]
# listComp : 1.23644 => [10..10009]
# mapCall  : 2.08971 => [10..10009]
# genExpr  : 2.72674 => [10..10009]
# genFunc  : 3.38200 => [10..10009]