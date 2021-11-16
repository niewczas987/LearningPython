class Spam:
    def __init__(self):
        self.data1 = 'jedzenie'

X=Spam()
print(X)

from lister import ListInstance
class Spam(ListInstance):
    def __init__(self):
        self.data = 'food'

X=Spam()
print(X)
