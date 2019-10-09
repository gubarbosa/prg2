def mes_extenso(data):
    meses = {
        1: 'Janeiro', 2: 'Fevereiro', 3: 'Marco', 4:'Abril', 5: 'Maio', 6: 'Junho', 7: 'Julho', 8: 'Agosto', 9:
        'Setembro', 10: 'Outubro', 11: 'Novembro', 12:'Dezembro'
    }
    dia, mes, ano = data.split('/')
    print('{} de {} de {}'.format(dia, meses[int(mes)], ano))


mes_extenso('21/2/2002')