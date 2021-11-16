#klasa podrzędna wbudowanego tylu list

class MyList(list):
    def __getitem__(self, item):
        print('(indeksowanie %s w pozycji %s)'%(self,item))
        return list.__getitem__(self,item-1)

if __name__=='__main__':
    print(list('abc'))
    x=MyList('abc')
    print(x)
    print(x[1])
    print(x[3])
    x.append('mielonka')
    print(x)
    x.reverse()
    print(x)