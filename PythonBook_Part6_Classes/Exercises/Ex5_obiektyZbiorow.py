#błąd z gfunkcją set - TypeError: 'Set' object is not iterable
from PythonBook_Part6_Classes.setwrapper import Set

class MultiSet(Set):
    def intersect(self,*others):
        res=[]
        for x in self:
            for other in others:
                if x not in other:
                    break
                else:
                    res.append(x)
        return Set(res)
    def union(*args):
        res=[]
        for seq in args:
            for x in seq:
                if not x in res:
                    res.append(x)
        return Set(res)

x = MultiSet([1,2,3,4])
y = MultiSet([3,4,5])
z = MultiSet([0,1,2])


x.intersect(y,z)