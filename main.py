# DECLARANDO FUNÇÕES

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return(imc)

def verificacao_imc(imc):
    if imc < 18.5:
        resultado = 'ABAIXO DO PESO'
    elif 18.5 <= imc <= 24.9:
        resultado = 'PESO NORMAL'
    elif 25 <= imc <= 29.9:
        resultado = 'SOBREPESO'
    elif 30 <= imc <= 34.9:
        resultado = 'OBESIDADE GRAU I'
    elif 35<= imc <= 39.9:
        resultado = 'OBESIDADE GRAU II (SEVERA)'
    else:
        resultado = 'OBESIDADE GRAU III (MÓRBIDA)'
    return resultado
    
def calcular_eer(sexo, idade, peso, altura, fa):
    if sexo == 'M':
        eer = 662 - (9.53 * idade) + fa * ((15.91 * peso) + (539.6 * altura))
        return eer
    else:
        eer = 354 - (6.91 * idade) + fa * ((9.36 * peso) + (726 * altura))
        return eer

def relatorio_inicial():
    print(f'{' DADOS INICIAIS ':-^60}')
    print(f'Nome: {nome}')
    print(f'Sexo: {'Masculino' if sexo == 'M' else 'Feminino'}')
    print(f'Idade: {idade}')
    print(f'Altura: {altura:.2f}m')
    print(f'Peso: {peso:.1f}kg')
    print(f'Nivel de At. Física: {fatoratv}')

def relatorio_final():
    print(f'{' RELATÓRIO FINAL ':=^60}')
    print(f'Nome: {nome}')
    print(f'Sexo: {'Masculino' if sexo == 'M' else 'Feminino'}')
    print(f'Idade: {idade} anos')
    print(f'Altura: {altura:.2f}m')
    print(f'Peso: {peso:.1f}kg')
    print(f'Nivel de At. Física: {fatoratv}')
    print('-'*60)
    print(f'O seu Índice de massa corporal é de {imc:.2f}kg/m², o que indica \nque você no momento está em {estado}.')
    print(f'O EER calculado é de {eer:.2f} kcal por dia.')
    if estado in ('SOBREPESO', 'OBESIDADE GRAU I', 'OBESIDADE GRAU II (SEVERA)', 'OBESIDADE GRAU III (MÓRBIDA)'):
        print(f"Estimativa de ajuste calórico: aproximadamente {eer - 500:.0f} kcal/dia.\npara PERDA de peso.")
    elif estado == 'ABAIXO DO PESO':
        print(f"Estimativa de ajuste calórico: aproximadamente {eer + 500:.0f} kcal/dia.\npara GANHO de peso.")
    else:
        if objetivo == 'GANHAR':
            print(f"Estimativa de ajuste calórico: aproximadamente {eer + 500:.0f} kcal/dia.\npara GANHO de peso.")
        elif objetivo == 'MANTER':
            print(f"Estimativa de ajuste calórico: aproximadamente {eer:.0f} kcal/dia.\npara MANTER o peso.")
        else:
            print(f"Estimativa de ajuste calórico: aproximadamente {eer - 500:.0f} kcal/dia.\npara PERDER o peso.")
    print('-'*60)
    recomendação(estado)
    print('='*60)

def recomendação(resultado):
    if resultado == 'ABAIXO DO PESO':
        print('Procure manter uma alimentação equilibrada e, se necessário, \nbusque orientação de um nutricionista.')
    elif resultado == 'PESO NORMAL':
        print('Continue mantendo uma alimentação equilibrada e praticando \natividades físicas regularmente.')
    elif resultado == 'SOBREPESO':
        print('Procure melhorar os hábitos alimentares e manter uma rotina \nregular de atividades físicas.')
    elif resultado == 'OBESIDADE GRAU I':
        print('Considere buscar orientação de um profissional de saúde para \nmelhorar a alimentação e os hábitos de vida.')
    elif resultado == 'OBESIDADE GRAU II (SEVERA)':
        print('É recomendado buscar acompanhamento profissional para avaliar \nalimentação, atividade física e saúde geral.')
    else:
        print('Procure acompanhamento médico e nutricional para uma avaliação \nindividualizada e segura.')

while True:
    print('-='*30)
    print(f'{' CALCULADORA NUTRICIONAL ':-^60}')
    print('-='*30)

    nome = str(input('Digite o seu nome: ')).strip().title()
    sexo = str(input('Qual seu sexo? [M/F] ')).strip().upper()[0]
    idade = int(input('Qual a sua idade? '))
    peso = float(input('Digite seu peso em kg: '))
    altura = float(input('Digite sua altura em metros: '))

    # FA -> FATOR ATIVIDADE
    respfa = fa = 0
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
            fa = 1.0
            
        elif respfa == 2:
            fatoratv = 'Pouco Ativo'
            fa = 1.11
            
        elif respfa == 3:
            fatoratv = 'Ativo'
            if sexo == 'M':
                fa = 1.25
                
            else:
                fa = 1.27
                
        elif respfa == 4:
            fatoratv = 'Muito ativo'
            if sexo == 'M':
                fa = 1.48
                
            else:
                fa = 1.45
                
        else:
            print('Não foi possível identificar. Tente novamente!')
            print('-'*60)

    escolha = 'nula'
    print('-'*60)
    while escolha not in ('1','2','3'):
        escolha = str(input('''Qual o seu objetivo?
        [1] Ganhar peso/massa
        [2] Manter peso/massa
        [3] Perder peso/massa
        Digite aqui: '''))
        if escolha == '1':
            objetivo = 'GANHAR'
        elif escolha == '2':
            objetivo = 'MANTER'
        elif escolha == '3':
            objetivo = 'PERDER'
        else:
            print('Resposta inválida, tente outra vez.')
            print('-'*60)
            
    imc = calcular_imc(peso, altura)
    eer = calcular_eer(sexo, idade, peso, altura, fa)
    estado = verificacao_imc(imc)
    relatorio_final()

    continuar = 'nulo'
    while continuar not in ('S', 'N'):
        continuar = str(input('Deseja fazer outro cálculo? [S/N] ')).upper().strip()[0]
        if continuar not in ('S', 'N'):
            print('Resposta inválida. Tente outra vez!')
    if continuar == 'N':
        break
print(f'{' PROGRAMA ENCERRADO ':/^60}')
