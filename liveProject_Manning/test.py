def f(d):
    L = []
    for k in d.keys():
        v=d[k]
        if type(k) is str:
            L.append(v)
    return L

a={'a':1,'b':2,1:8}
print(f(a))