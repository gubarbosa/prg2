def conta_palavras(texto):
    texto = "um texto qualquer para estee teste de um contador de palavras em um texto"
    texto = texto.split()
    dicionario = {}
    for palavra in texto:
            dicionario[palavra] = texto.count(palavra)
    print(dicionario)


