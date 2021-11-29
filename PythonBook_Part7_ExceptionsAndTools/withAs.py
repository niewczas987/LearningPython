# składnia
# with wyrazenie [as zmienna]:
#     blok_with
import decimal

with decimal.localcontext() as ctx:
    ctx.prec =2
    x= decimal.Decimal('1.00')/decimal.Decimal(3.00)
    #print(x)

class TraceBlock:
    def message(self,arg):
        print('wykonanie',arg)
    def __enter__(self):
        print('rozpoczecie bloku')
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print('normalne wyjscie\n')
        else:
            print('zgloszenie wyjatku!',exc_type)
            return False

with TraceBlock() as action:
    action.message('test1')
    print('osiagniety')

# with TraceBlock() as action:
#     action.message('test2')
#     raise TypeError
#     print('nie zostal osiagniety')