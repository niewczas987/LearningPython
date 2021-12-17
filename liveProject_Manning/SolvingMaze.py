'''
Legend:
# - maze wall
o - start point
x - empty point, unvisited
'''
#imports
import csv
import random
from colorama import init, Fore

#function:
'''
function generating maze fields.
'''
def buildMaze(width, height):
    result = []
    for i in range(0, height):
        line = []
        for j in range(0, width):
            line.append(empty)
        result.append(line)
    return result

'''
Function for grafical presentation in console.
'''
def print_maze(maze):
    for i in range(0, len(maze)):
        for j in range(0, len(maze[0])):
            if maze[i][j] == empty:
                print(Fore.WHITE, f'{maze[i][j]}', end="")
            elif maze[i][j] == cell:
                print(Fore.GREEN, f'{maze[i][j]}', end="")
            else:
                print(Fore.RED, f'{maze[i][j]}', end="")
        print('\n')

'''
Make sure that every wall that we are going to turn into passage, 
does not have more than one cell around it. 
If  this kind of check is not made, it will end up 
with a maze that has clusters of passages
'''
def surrCells(rand_walls):
    cellsCount = 0
    if (maze[rand_walls[0] - 1][rand_walls[1]] == cell):
        cellsCount += 1
    if (maze[rand_walls[0] + 1][rand_walls[1]] == cell):
        cellsCount += 1
    if (maze[rand_walls[0]][rand_walls[1] - 1] == cell):
        cellsCount += 1
    if (maze[rand_walls[0]][rand_walls[1] + 1] == cell):
        cellsCount += 1
    return cellsCount
'''
Remove processed block from the walls list
'''
def deleteWall(walls):
    for wall in walls:
        if (wall[0] == random_wall[0] and wall[1] == random_wall[1]):
            walls.remove(wall)
'''
Make unvisited cells walls.
'''
def makeWalls(width,height):
    for i in range(0,height):
        for j in range(0,width):
            if maze[i][j] == empty:
                maze[i][j] = wall

'''
create entrance and exit
'''
def createEntranceExit(width, height):
    for i in range(0,width):
        if maze[1][i] == cell:
            maze[0][i] = cell
            break
    for i in range(width-1, 0 ,-1):
        if maze[height-2][i] == cell:
            maze[height-1][i] = cell
            break

'''
MAIN PROGRAM
'''
if __name__ == '__main__':
    # variables
    cell = ' '
    wall = '#'
    empty = 'X'
    height = 11
    width = 27
    start_h = int(random.random() * height)
    start_w = int(random.random() * width)
    # setting edge conditions for the starting point
    if start_h == 0:
        start_h += 1
    elif start_h == height - 1:
        start_h -= 1
    if start_w == 0:
        start_w += 1
    elif start_w == height - 1:
        start_w -= 1

    #initialize colorama
    init()

    # print('START H:',start_h,'\nSTART W:',start_w)
    # building maze
    maze = buildMaze(width, height)
    # print_maze(maze)

    maze[start_h][start_w] = cell
    # print_maze(maze)
    walls = []
    walls.append([start_h - 1, start_w])
    walls.append([start_h + 1, start_w])
    walls.append([start_h, start_w - 1])
    walls.append([start_h, start_w + 1])
    # print('WALLS\n',walls)
    # denote the blocks around starting cell as walls
    maze[start_h - 1][start_w] = wall
    maze[start_h + 1][start_w] = wall
    maze[start_h][start_w + 1] = wall
    maze[start_h][start_w - 1] = wall
    # print('MAZE\n', walls)
    #While there are walls in the list pick a random wall from the list
    '''
    Check the blocks to the left and right of the wall we are processing 
    and then we need to check the blocks above and below the wall.
    Make sure that you are always accessing a correct index. 
    Meaning that if the selected wall is the one on the first line of the maze, 
    we cannot go and check the cell above it, since it would create an 'IndexError'
    '''
    while walls:
        #pick random wall
        random_wall = walls[int(random.random()*len(walls))-1]
        #check if it's left wall
        if random_wall[1]!=0:
            if (maze[random_wall[0]][random_wall[1]-1] == empty and maze[random_wall[0]][random_wall[1]+1] == cell):
                #find number of surro=unding cells
                s_cells = surrCells(random_wall)
                if s_cells <2:
                    #denote new path
                    maze[random_wall[0]][random_wall[1]] = cell
                    #mark new walls
                    #upper cell
                    if (random_wall[0] != 0):
                        if (maze[random_wall[0] - 1][random_wall[1]] != cell):
                            maze[random_wall[0] - 1][random_wall[1]] = wall
                        if ([random_wall[0] - 1, random_wall[1]] not in walls):
                            walls.append([random_wall[0] - 1, random_wall[1]])
                    #bottom cell
                    if (random_wall[0] != height-1):
                        if (maze[random_wall[0] + 1][random_wall[1]] != cell):
                            maze[random_wall[0] - 1][random_wall[1]] = wall
                        if ([random_wall[0] + 1, random_wall[1]] not in walls):
                            walls.append([random_wall[0] + 1, random_wall[1]])
                    #left-most cell
                    if (random_wall[1] != 0):
                        if (maze[random_wall[0]][random_wall[1]-1] != cell):
                            maze[random_wall[0]][random_wall[1]-1] = wall
                        if ([random_wall[0], random_wall[1]-1] not in walls):
                            walls.append([random_wall[0], random_wall[1]-1])

                #delete wall
                deleteWall(walls)
                continue
        #check if it is an upper wall
        if random_wall[0] != 0:
            if (maze[random_wall[0]-1][random_wall[1]] == empty and maze[random_wall[0]+1][random_wall[1]] == cell):
                s_cells = surrCells(random_wall)
                if s_cells < 2:
                    #denote the new path
                    maze[random_wall[0]][random_wall[1]] = cell
                    #mark new walls
                    #upper
                    if (random_wall[0] != 0):
                        if (maze[random_wall[0] - 1][random_wall[1]] != cell):
                            maze[random_wall[0] - 1][random_wall[1]] = wall
                        if ([random_wall[0] - 1, random_wall[1]] not in walls):
                            walls.append([random_wall[0] - 1, random_wall[1]])
                    #left-most
                    if (random_wall[1] != 0):
                        if (maze[random_wall[0]][random_wall[1]-1] != cell):
                            maze[random_wall[0]][random_wall[1]-1] = wall
                        if ([random_wall[0], random_wall[1]-1] not in walls):
                            walls.append([random_wall[0], random_wall[1]-1])
                    #right-most
                    if (random_wall[1] != width-1):
                        if (maze[random_wall[0]][random_wall[1]+1] != cell):
                            maze[random_wall[0]][random_wall[1]+1] = wall
                        if ([random_wall[0], random_wall[1]+1] not in walls):
                            walls.append([random_wall[0], random_wall[1]+1])

                #delete wall
                deleteWall(walls)
                continue
        #check if it is an bottom wall
        if random_wall[0] != height - 1:
            if (maze[random_wall[0]+1][random_wall[1]] == empty and maze[random_wall[0]-1][random_wall[1]] == cell):
                s_cells = surrCells(random_wall)
                if s_cells < 2:
                    #denote the new path
                    maze[random_wall[0]][random_wall[1]] = cell
                    #mark new walls
                    #bottom cell
                    if (random_wall[0] != height-1):
                        if (maze[random_wall[0] + 1][random_wall[1]] != cell):
                            maze[random_wall[0] + 1][random_wall[1]] = wall
                        if ([random_wall[0] + 1, random_wall[1]] not in walls):
                            walls.append([random_wall[0] + 1, random_wall[1]])
                    #left-most
                    if (random_wall[1] != 0):
                        if (maze[random_wall[0]][random_wall[1] - 1] != cell):
                            maze[random_wall[0]][random_wall[1] - 1] = wall
                        if ([random_wall[0], random_wall[1] - 1] not in walls):
                            walls.append([random_wall[0], random_wall[1] - 1])
                    #right-most
                    if (random_wall[1] != width-1):
                        if (maze[random_wall[0]][random_wall[1]+1] != cell):
                            maze[random_wall[0]][random_wall[1]+1] = wall
                        if ([random_wall[0], random_wall[1]+1] not in walls):
                            walls.append([random_wall[0], random_wall[1]+1])

                #delete wall
                deleteWall(walls)
                continue
        # check if it's right wall
        if random_wall[1] != width - 1:
            if (maze[random_wall[0]][random_wall[1]+1] == empty and maze[random_wall[0]][random_wall[1]-1] == cell):
                s_cells = surrCells(random_wall)
                if s_cells < 2:
                    #denote the new path
                    maze[random_wall[0]][random_wall[1]] = cell
                    #mark new walls
                    # right-most
                    if (random_wall[1] != width - 1):
                        if (maze[random_wall[0]][random_wall[1] + 1] != cell):
                            maze[random_wall[0]][random_wall[1] + 1] = wall
                        if ([random_wall[0], random_wall[1] + 1] not in walls):
                            walls.append([random_wall[0], random_wall[1] + 1])
                    # upper
                    if (random_wall[0] != 0):
                        if (maze[random_wall[0] - 1][random_wall[1]] != cell):
                            maze[random_wall[0] - 1][random_wall[1]] = wall
                        if ([random_wall[0] - 1, random_wall[1]] not in walls):
                            walls.append([random_wall[0] - 1, random_wall[1]])
                    # bottom cell
                    if (random_wall[0] != height - 1):
                        if (maze[random_wall[0] + 1][random_wall[1]] != cell):
                            maze[random_wall[0] + 1][random_wall[1]] = wall
                        if ([random_wall[0] + 1, random_wall[1]] not in walls):
                            walls.append([random_wall[0] + 1, random_wall[1]])

                #delete wall
                deleteWall(walls)
                continue
        #delete the wall from list anyway
        deleteWall(walls)
    makeWalls(width,height)
    createEntranceExit(width,height)
    print_maze(maze)

    # with open('GFG', 'w') as f:
    #
    #     # using csv.writer method from CSV package
    #     write = csv.writer(f)
    #     write.writerows(maze)