'''
Legend:
# - maze wall
o - start point
x - exit point
'''
#imports
import random


def buildMaze(width,height):
    result =[]
    for x in range(0, height):
        if x==0:
            result.append('#'*width)
        elif x==height-1:
            result.append('#'*width)
        else:
            wall = '#' + ' '*(width-2) +'#'
            for c in wall[1:-1]:
                pass


            result.append(wall)

    return result


def buildMaze2(width, height):
    result = []
    for x in range(0, height):
        if x == 0:
            result.append('#' * width)
        elif x == height - 1:
            result.append('#' * width)
        else:
            wall = '#'* width
            res = ''
            for c in wall[1:-1]:
                print(c)
                if random.randint(0,1):
                    res+='#'
                else:
                    res+=' '
            wall = '#'+res+'#'
            print('Wall',wall)

            result.append(wall)

    return result


#building maze
maze = buildMaze2(10,10)




if __name__ == '__main__':
    for x in maze:
        print(x)
