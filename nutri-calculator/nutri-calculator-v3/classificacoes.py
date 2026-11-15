# classificacoes.py

def verificacao_imc(imc):
    if imc < 18.5:
        resultado = 'ABAIXO DO PESO'
    elif 18.5 <= imc < 25:
        resultado = 'PESO NORMAL'
    elif 25 <= imc < 30:
        resultado = 'SOBREPESO'
    elif 30 <= imc < 35:
        resultado = 'OBESIDADE GRAU I'
    elif 35<= imc < 40:
        resultado = 'OBESIDADE GRAU II (SEVERA)'
    else:
        resultado = 'OBESIDADE GRAU III (MÓRBIDA)'
    return resultado
