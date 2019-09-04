print('-----------JOGO DOS TIMES DO BRASILEIRÃO 2019----------')
arquivo = open('palavras.txt', encoding='utf-8')
import random
linha = open('palavras.txt').read().splitlines()
linha_aleatoria = random.choice(linha)
palavra = "".join(random.sample(linha_aleatoria, len(linha_aleatoria)))
frases_motivadoras = 'Você é o cara!, não desista, a insistência leva a perfeição, um ganhador só ganha quando não perde /n',
'Você consegue maninho!, nada como um dia após o outro!, Palmeiras não tem mundial!'
print('O jogo consiste em adivinhar qual é o time correto, sendo que você receberá a palavra de forma embaralhada, tendo 5 tentativas para descobrir!')

tentativas = 5
while tentativas != 0:
    print('A palavra embaralhada é {}'.format(palavra, tentativas))
    resp = input('Você ainda possui {} tentativas, digite sua tentativa:'.format(tentativas))
    tentativas -= 1
    if resp == linha_aleatoria and tentativas == 5:
        print('Parabéns, a palavra embaralhada é {} e você acertou de primeira!'.format(linha_aleatoria))
        break
    elif resp == linha_aleatoria:
        print('Parabéns, a palavra é {} e você ganhou o jogo utilizando {} tentativas'.format(linha_aleatoria, 5 - tentativas))
        break
    else:
        print(frases_motivadoras)
else:
    print('A palavra correta era {}, e você utilizou {} tentativas '.format(linha_aleatoria, 5 - tentativas))

print('-----FIM DO JOGO------')

