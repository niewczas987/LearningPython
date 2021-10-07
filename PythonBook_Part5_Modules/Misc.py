"""
import sys
print(sys.path) #sprawdzenie PYTHONPATH
"""


'''
creating .pth file
'''
# site_packages_path is the packages folder, which in my case is:
site_packages_path = r'C:\Users\PLKANIE3\Documents\KN\Python\site_packages'
# path that you wanna add, which again in my case is
path_to_add = r'C:\Users\PLKANIE3\PycharmProjects\LearningPython\PythonBook_Part1'

f = open(site_packages_path + '\custom_path.pth', 'a')
f.write(path_to_add)