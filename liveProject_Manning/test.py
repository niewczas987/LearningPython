def f(d):
    L = []
    for k in d.keys():
        v=d[k]
        if type(k) is str:
            L.append(v)
    return L

a={'a':1,'b':2,1:8}
print(f(a))



def init_maze(width, height):
    maze = []
    for i in range(0, height):
        line = []
        for j in range(0, width):
            line.append('u')
        maze.append(line)
    return maze

print(init_maze(10,10))