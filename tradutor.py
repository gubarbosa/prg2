dicionario = {"batatafrita": "frenchfries", "hambúrguer": "hamburguer", "cocacola": "coke",
              "eu": "I", "quero": "want", "e": "and", "com": "with", "carne": "meat", "queijo": "cheese", "para": "for", "hoje": "today", "comer": "eat"}


def traduz_para_ingles(texto):
    for item in dicionario:
        for palavra in texto:
            if item.lower() == palavra.lower():
                novo_texto = texto.replace(palavra, dicionario[item])
            else:
                pass
    return novo_texto