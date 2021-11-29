def action2():
    print(1+[])

def action1():
    try:
        action2()
    except TypeError:
        print('Wewnetrzne try')


try:
    action1()
except TypeError:
    print('zewnetrzne try')