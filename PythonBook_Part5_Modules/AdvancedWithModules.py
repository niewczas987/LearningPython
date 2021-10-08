#testy jednostkowe z __name__
print('jestem',__name__)

def minmax(test, *args):
    res = args[0]
    for arg in args[1:]:
        if test(arg,res):
            res = arg
    return res

def lessThan(x,y): return x<y
def grtrThan(x,y):return x>y

if __name__ == '__main__':
    print(minmax(lessThan,4,2,1,5,6,3))
    print(minmax(grtrThan,4,2,1,5,6,3))

def commas(N):
    digits = str(N)
    assert(digits.isdigit())
    result=''
    while digits:
        digits, last3 = digits[:-3],digits[-3:]
        result = (last3+','+result) if result else last3
    return result

def money(N, width = 0):
    sign = '-' if N<0 else ''
    N = abs(N)
    whole = commas(int(N))
    fract = ('%.2f'%N)[-2:]
    format = '%S%S.%S'%(sign,whole,fract)
    return '$%*s'%(width,format)

#rozszerzanie syspath
import sys
print(sys.path)
sys.path.append('C:\\temp')
print(sys.path)


#funkcja reload all
import types
from importlib import reload

def status(module):
    print('przełądowanie',module.__name__)

def transitive_reload(module, visited):
    if not module in visited:
        status(module)
        reload(module)
        visited[module]=None
        for attrobj in module.__dict__.values():
            if type(attrobj) == types.ModuleType:
                transitive_reload(attrobj,visited)
def reload_all(*args):
    visited={}
    for arg in args:
        if type(arg) == types.ModuleType:
            transitive_reload(arg,visited)
if __name__ == '__main__':
    reload_all(reload_all)