print('hi from GUI init\n')
from Python_GUI_Cookbook.Ch11_Best_Practices.Folder1.Folder2.Folder3.MessageBox import clickMe
from sys import path
from pprint import pprint
# Required setup for the PYTHONPATH in order to find all package folders
from site import addsitedir
from os import getcwd, chdir, pardir
while True:
    curFull = getcwd()
    curDir = curFull.split('\\')[-1]
    if 'Ch11_Best_Practices' == curDir:
        addsitedir(curFull)
        addsitedir(curFull + 'Folder1\Folder2\Folder3')
        break
    chdir(pardir)
pprint(path)