#%% 
# https://stackoverflow.com/questions/27792008/python-create-recursive-folder-structure

'''
I'm writing a script to automate the creation of a test file/folder structure - input for another script (to move only some files according to a file list). My code below works, but is there a more pythonic way to complete the same task?
'''


import os
import shutil

os.chdir('c:/')

if not os.path.exists('c:/pythontest'):
    os.mkdir('c:/pythontest')
else:
    shutil.rmtree('c:/pythontest')
    os.mkdir('c:\pythontest')

os.chdir('c:/pythontest')

for i in range(0,3):
    os.mkdir('folder%d' % i)
    fileName = 'folder%d' % i
    filePath = os.path.join(os.curdir, fileName)
    print filePath
    os.chdir(filePath)
    for j in range(0,3):
        os.mkdir('folder%d_%d' % (i,j))
        fileName = 'folder%d_%d' % (i,j)
        filePath = os.path.join(os.curdir, fileName)
        print str(filePath)
        os.chdir(filePath)
        for k in range(0,3):
            try:
                f = open('file%d_%d_%d.txt' % (i,j,k), 'w')
            except IOError:
                pass
        os.chdir('..')
    os.chdir('..')

## VERSION 2: I can only suggest several minor style improvements -- and moving everything within a function, which speeds things up.

import os
import shutil

def doit():
    shutil.rmtree('c:/pythontest', ignore_errors=True)
    os.mkdir('c:/pythontest')
    os.chdir('c:/pythontest')

    for i in range(0,3):
        fileName = 'folder%d' % i
        print fileName
        os.mkdir(fileName)
        os.chdir(fileName)
        for j in range(0,3):
            fileName = 'folder%d_%d' % (i,j)
            print fileName
            os.mkdir(fileName)
            os.chdir(fileName)
            for k in range(0,3):
                try:
                    with open('file%d_%d_%d.txt' % (i,j,k), 'w'):
                        pass
                except IOError:
                    pass
            os.chdir('..')
        os.chdir('..')

'''
The minor but cumulative improvements include avoidance of repetition, and avoidance of redundancy (such as prepending a './' to filenames to make exactly equivalent filepaths).
'''

