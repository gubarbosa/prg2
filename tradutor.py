dicionario = {"batatafrita": "frenchfries", "hambúrguer": "hamburguer", "cocacola": "coke",
              "eu": "I", "quero": "want", "e": "and", "com": "with", "carne": "meat", "queijo": "cheese", "para": "for", "hoje": "today", "comer": "eat"}

frase = 'eu quero comer hambúrguer com queijo e carne para hoje'
x = []

def traduz_para_ingles(frase):
    frase_arr = frase.split()
    for palavra in frase_arr:
        for i in dicionario.keys():
            if palavra.lower() == i.lower():
                x.append(dicionario[i])

    return " ".join(x)

traducao = traduz_para_ingles(frase)
print(traducao)