arquivo = open('musica.txt', 'w')
arquivo.writelines("Nova música 1")      #Esse trecho abre um txt e escreve no mesmo.
arquivo.close()

arquivo = open('musica1.txt', 'r')
musicas = arquivo.readlines()            #Esse trecho abre um txt e faz uma lista onde cada linha é um elemento dela.
print(musicas)

arquivo = open('musica2.txt', 'a')
arquivo.writelines('Nova música 2')      #Esse trecho abre um txt e adiciona o que está escrito no txt.
arquivo.close()