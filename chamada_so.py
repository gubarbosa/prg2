import os
import platform
sistema = platform.system()

def verDiretorio():
    if sistema == 'Windows':
        os.system('dir')
    else:
        os.system('ls')

verDiretorio()