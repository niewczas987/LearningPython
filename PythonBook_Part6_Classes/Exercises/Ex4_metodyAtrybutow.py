#ma=etody atrybutów
class Meta:
    def __getattr__(self,name):
        print('pobierz', name)
    def __setattr__(self,name,value):
        print('ustaw',name,value)

x = Meta()
x.append
x.spam = 'pork'