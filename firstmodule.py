'''
 What is Python Module?
    -->Python is nothing but Python module.i.e (.py file is python module.)

Why we use python module?
    --> Module are use to divide the large and complex program in multiple files and allow to integrate them.

There are 2 types of modules
1. Built-in-Module.
        1.1 Core Python Module
              math,os,datetime,pickle etc....
        1.2 Extended Python Module
              The module which we want to install using PIP(Python Installer Package) command is known as extended python module.
                
              syntax for installation:
                    python -m pip install module_name
2. Custom Module /User defined module
    -->The module or Python files created by the user is known as python module.
    -->e.g. Current python file i.e(firstmodule) is cuatom module
    --> In other words Python module is collection of variables, function and classes.

HOW TO ACCESS ANY MODULE:
    --> To access any module we have to import it first.
    --> SYNTAX: 
            import module_name
        or
            import module_name as temp_name  #here temp - temproary name 

TO ACCESS VARIABLE AND FUNCTION FROM IMPORTED MODULE
        module_name.variable_name
        module_name.function_name()

'''
#1st Method

import math
print('PI :-',math.pi)   #variable
print('Power:- ',math.pow(2,5))   #function

#2nd Method(using alise)

import math as m
print('PI :-',m.pi)   #variable
print('Power:- ',m.pow(2,5))   #function

#OS - MODULE : it perform operation related to OS.

import os
print('Current Working Directory',os.getcwd())
print('List of List in CWD',os.listdir())
#print('List of file in specific directory',os.listdir(r'C:\Hemang'))

#To make a single directory
'''
os.mkdir('demo')
print('Demo folder created in in CWD')
'''

#To make a multiple directory or nested folder
#os.makedirs('a_folder/b_folder')   

#To delete/remove any file
'''
os.remove(r'demo/test.txt')
print('File Is deleted successfully!!!!!!!!')
'''

#To delete / remove folder
os.rmdir('demo')
print('Folder is deleted Successfully')

#To rename folder
'''
os.rename(oldname,newname)
It is used to change the name of specified file or dir
'''