# entradas.py

def verificador_bebe(idade):
    if idade < 3:
        print('-'*60)
        print('Detectamos que esta pessoa tem menos que 3 anos de idade,\nportanto, o cálculo é feito com mais cuidado.')
        print('Para darmos segmento, por favor, informe quantos meses de \nidade.')
        print('''Exemplo:
        [3] para três meses de idade
        [8] para oito meses de idade
        [12] para doze meses ou um ano de idade
        [18] para dezoito meses ou um ano e meio
        ...''')
        meses = int(input('Digite aqui: '))
        print(f'Identificamos que o bebê tem {meses} meses de idade.')
        return meses
    else:
        return None

def escolher_fator_atividade():
# FATOR ATIVIDADE
    respfa = 0
    fatoratv = ''
    print('-'*60)
    while respfa not in (1, 2, 3, 4):
        respfa = int(input('''Informe qual o seu Fator Atividade:
        [1] Sedentário
        [2] Pouco Ativo
        [3] Ativo
        [4] Muito Ativo
        Digite aqui: '''))
        if respfa == 1:
            fatoratv = 'Sedentário'
        elif respfa == 2:
            fatoratv = 'Pouco Ativo'
        elif respfa == 3:
            fatoratv = 'Ativo'
        elif respfa == 4:
            fatoratv = 'Muito ativo'
        else:
            print('Não foi possível identificar. Tente novamente!')
            print('-'*60)
    return fatoratv