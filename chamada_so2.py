import os
import platform
sistema = platform.system()

def verDiretorio():
    if sistema == 'Windows':
        os.system('dir Macacos')
    else:
        os.system('ls')

def criarPasta():
    os.system('mkdir Macacos')


criarPasta()
verDiretorio()
