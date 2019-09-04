mantimentos = ["banana", "laranja", "melao", "pera"]
estoque = {"banana": 6, "melao": 0, "laranja": 32, "pera": 15}
precos = {"banana": 4, "melao": 2, "laranja": 1.5, "pera": 3}

def calcular_conta(mantimentos):
    preco_total = 0
    for i in estoque:
        if estoque[i] > 0:
            preco_total += precos[i]
            estoque[i] -= 1
        else:
            pass
    return print('Conta total: {} | Estoque: {}'.format(preco_total, estoque))