import os
import platform
sistema = platform.system()

def dir():
    if sistema == 'Windows':
        os.system('dir')
    else:
        os.system('ls')

dir()