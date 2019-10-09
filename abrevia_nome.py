def abrevia_nome(nome):
    nome_split = nome.split()
    nome_novo = nome_split[0], nome_split[-1]
    abreviatura = []

    for palavra in nome_split:
        if palavra not in nome_novo and len(palavra) > 2:
            abreviatura.append(palavra[0])

    abreviatura = ' '.join(abreviatura)

    print('{} {} {}'.format(nome_split[0], abreviatura, nome_split[-1]))


abrevia_nome('Gustavo Barbosa Queiroz da Espindula')