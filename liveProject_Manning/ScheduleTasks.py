#imports
from random import randrange
from itertools import permutations
#variables
tasks=[]
taskList = {}
timeInDay=4 #time in hours

#classes
'''
Creating taskList data structure.
{ 'taskName': (totalTime, burst) }
where:
- totalTime - how long task will take (in hours)
- burst - how many times task could be broken up
'''
class addTask(dict):
    def __init__(self):
        self = dict()
    def add(self,key,value):
        try:
            if len(value)!=2:
                raise AttributeError
            else:
                self[key] = value
        except:
            raise TypeError

#functions
'''
all_task_subsets
Function that create all tasks combinations - permutations.
Returns generator object of all possible combinations of the task.
Created based on itertools.permutations
'''
def all_task_subsets(taskList):
    permut = permutations(taskList, len(taskList))
    # print(*permut,sep='\n')
    return permut
'''
min_time_left
Function takes all tasks in task subsets from 'all_task_subset' function that match
the criteria to minimize the time leftover in a day. 
'''
def min_time_left(permut):
    for taskSubset in permut:
        print('Variation:',taskSubset)
        subsetWithValues = {k:taskList[k] for k in taskSubset}
        timeOfTheSubset = 0
        for task in subsetWithValues:
            timeTheTaskTakes = manageTasks(task, subsetWithValues[task][0], subsetWithValues[task][1])
            # print('Task:',task,'.Time it takes:',timeTheTaskTakes[task])
            timeOfTheSubset += timeTheTaskTakes[task]
        if timeOfTheSubset <= timeInDay:
            print('Time of subset',timeOfTheSubset)
        else:
            print('Subset takes too long.')
            print('Time of subset', timeOfTheSubset)
            print(taskSubset)
        #getting optimal time of subset
        optimalTime = timeInDay - timeOfTheSubset
        if optimalTime > 0:
            optimalTime = timeOfTheSubset
    if optimalTime == timeInDay:
        print('-'*30,'\nNo valid subset for this tasks.')
    else:
        print('-'*30,'\nOptimal time:',optimalTime,'\nTask subset:',taskSubset)

'''
manageTasks
For every task in the input, calculate the time it takes as the total time 
allocated to a task divided by the number of blocks you can divide the time into.
Function should return the new data structure.
'''
def manageTasks(task, totalTime, nrOfBlks):
    if nrOfBlks>0:
        taskTime = totalTime/nrOfBlks
    else:
        raise AttributeError
    return {task:taskTime}

#generate task list - for simulation purposes
for x in range(3):
    tasks.append('task'+str(x))


if __name__ == '__main__':

    # create data structure with generated task
    taskList = addTask()
    for task in tasks:
        taskList.add(task, (randrange(1, 6), randrange(1, 6)))
    print('-'*30)
    print('TASK LIST')
    for k in taskList.keys():
        print('Task name:',k,'\nTotal time:',taskList[k][0],'\nNumber of bursts:',taskList[k][1])
    permut = all_task_subsets(taskList)
    # print(*permut,sep='\n')
    print('-' * 30)
    print('MIN TIME LEFT')
    min_time = min_time_left(permut)