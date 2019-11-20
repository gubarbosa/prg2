import os
import platform

usuario = int(input('[1] - Informacoes do sistema \n'
                    '[2] - Uso do disco \n'
                    '[3] - Solicita host e retorna um ping host \n'
                    '[4] - Sair do sistema  \n'
                    'Opcao: ')) 
if usuario == 1:
    sistema = platform.system()
    machine = platform.machine()
    node = platform.node()
    plataforma = platform.platform()
    print(sistema, machine, node, plataforma)
elif usuario == 2:
    if platform.system() == "Windows":
        os.system('dir')
    elif platform.system() == "Linux": 
        os.system('df -h')
elif usuario == 3:
    host = str(input('Digite um host para pingar: '))
    comando_ping = 'ping ' + host
    os.system(comando_ping)
elif usuario == 4:
    pass