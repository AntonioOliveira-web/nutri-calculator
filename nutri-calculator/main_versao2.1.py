from time import sleep

# DECLARANDO FUNÇÕES

def calcular_imc(peso, altura):
    imc = peso / ((altura / 100) ** 2)
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

def conversao_idade(meses):
    idade_crianca = meses / 12 
    return idade_crianca

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
        idade_crianca = conversao_idade(meses)
        print(f'Identificamos que o bebê tem {meses} meses de idade.')
        return meses
    else:
        return None

def calcular_eer_crianca(idade_crianca, sexo, altura, peso):
    if 0 <= idade_crianca < 0.25:
        # GRUPO DE 0 MESES À 2.99 MESES
        if sexo == 'M':
            eer = -716.45 - (1.00 * idade_crianca) + (17.82 * altura) + (15.06 * peso) + 200
            return eer
        else:
            eer = -69.15 - (80.00 * idade_crianca) + (2.65 * altura) + (56.15 * peso) + 180
            return eer
        
    elif 0.25 <= idade_crianca < 0.5:
        # GRUPO DE 3 MESES À 5.99 MESES
        if sexo == 'M':
            eer = -716.45 - (1.00 * idade_crianca) + (17.82 * altura) + (15.06 * peso) + 50
            return eer
        else:
            eer = -69.15 + (80.00 * idade_crianca) + (2.65 * altura) + (54.15 * peso) + 60
            return eer        
        
    elif 0.5 <= idade_crianca < 3:
        # GRUPO DE 6 MESES À 2.99 ANOS
        if sexo == 'M':
            eer = -716.45 - (1.00 * idade_crianca) + (17.82 * altura) + (15.06 * peso) + 20
            return eer
        else:
            eer = -69.15 + (80.00 * idade_crianca) + (2.65 * altura) + (54.15 * peso) + (20 if 0.5 <= idade_crianca < 1.0 else  15)
            return eer
    return eer

def calcular_eer2(sexo, idade, peso, altura, fatoratv):

    if 3 <= idade < 14:
        # GRUPO DE CRIANÇAS DE 3 À 13.99 ANOS
        if sexo == 'M':
            # FÓRMULA MASCULINA
            if fatoratv == 'Sedentário':
                eer = -447.51 + (3.68 * idade) + (13.01 * altura) + (13.15 * peso) + (20 if 3 <= idade < 4 else 15 if 4 <= idade < 9 else 25)
                return eer
            elif fatoratv == 'Pouco Ativo':
                eer = 19.12 + (3.68 * idade) + (8.62 * altura) + (20.28 * peso) + (20 if 3 <= idade < 4 else 15 if 4 <= idade < 9 else 25)
                return eer
            elif fatoratv == 'Ativo':
                eer = -388.19 + (3.68 * idade) + (12.66 * altura) + (20.46 * peso) + (20 if 3 <= idade < 4 else 15 if 4 <= idade < 9 else 25)
                return eer
            else:
                eer = -671.75 + (3.68 * idade) + (15.68 * altura) + (23.25 * peso) + (20 if 3 <= idade < 4 else 15 if 4 <= idade < 9 else 25)
                return eer
        else:
            # FÓRMULA FEMININA
            if fatoratv == 'Sedentário':
                eer = 55.69 - (22.25 * idade) + (8.43 * altura) + (17.07 * peso) + (15 if 3 <= idade < 4 else 15 if 4 <= idade < 9 else 30)
                return eer
            elif fatoratv == 'Pouco Ativo':
                eer = -297.54 - (22.25 * idade) + (12.77 * altura) + (14.73 * peso) + (15 if 3 <= idade < 4 else 15 if 4 <= idade < 9 else 30)
                return eer
            elif fatoratv == 'Ativo':
                eer = -189.55 - (22.25 * idade) + (11.74 * altura) + (18.34 * peso) + (15 if 3 <= idade < 4 else 15 if 4 <= idade < 9 else 30)
                return eer
            else:
                eer = -709.59 - (22.25 * idade) + (18.22 * altura) + (14.25 * peso) + (15 if 3 <= idade < 4 else 15 if 4 <= idade < 9 else 30)
                return eer
     
    elif 14 <= idade < 19:
        # GRUPO DE ADOLECENTES DE 14 À 18.99 ANOS
        if sexo == 'M':
            # FÓRMULA MASCULINA
            if fatoratv == 'Sedentário':
                eer = -447.51 + (3.68 * idade) + (13.01 * altura) + (13.15 * peso) + 20
                return eer
            elif fatoratv == 'Pouco Ativo':
                eer = 19.12 + (3.68 * idade) + (8.62 * altura) + (20.28 * peso) + 20
                return eer
            elif fatoratv == 'Ativo':
                eer = -388.19 + (3.68 * idade) + (12.66 * altura) + (20.46 * peso) + 20
                return eer
            else:
                eer = -671.75 + (3.68 * idade) + (15.68 * altura) + (23.25 * peso) + 20
                return eer
        else:
            # FÓRMULA FEMININA
            if fatoratv == 'Sedentário':
                eer = 55.69 - (22.25 * idade) + (8.43 * altura) + (17.07 * peso) + 20
                return eer
            elif fatoratv == 'Pouco Ativo':
                eer = -297.54 - (22.25 * idade) + (12.77 * altura) + (14.73 * peso) + 20
                return eer
            elif fatoratv == 'Ativo':
                eer = -189.55 - (22.25 * idade) + (11.74 * altura) + (18.34 * peso) + 20
                return eer
            else:
                eer = -709.59 - (22.25 * idade) + (18.22 * altura) + (14.25 * peso) + 20
                return eer

    else: # if idade >= 19:
        # GRUPO DE ADULTOS *ACIMA* DE 18 ANOS
        if sexo == 'M':
            # FÓRMULA MASCULINA
            if fatoratv == 'Sedentário':
                eer = 753.07 - (10.83 * idade) + (14.10 * peso) + (6.50 * altura)
                return(eer)
            elif fatoratv == 'Pouco Ativo':
                eer = 581.47 - (10.83 * idade) + (14.94 * peso) + (8.30 * altura)
                return(eer)
            elif fatoratv == 'Ativo':
                eer = 1004.82 - (10.83 * idade) + (15.91 * peso) + (6.52 * altura)
                return(eer)
            else:
                eer = -517.88 - (10.83 * idade) + (19.11 * peso) + (15.61 * altura)
                return(eer)
        else:
            # FÓRMULA FEMININA
            if fatoratv == 'Sedentário':
                eer = 584.90 - (7.01 * idade) + (11.71 * peso) + (5.72 * altura)
                return(eer)
            elif fatoratv == 'Pouco Ativo':
                eer = 575.77 - (7.01 * idade) + (12.14 * peso) + (6.60 * altura)
                return (eer)
            elif fatoratv == 'Ativo':
                eer = 710.25 - (7.01 * idade) + (12.34 * peso) + (6.54 * altura)
                return(eer)
            else:
                eer = 511.83 - (7.01 * idade) + (12.56 * peso) + (9.07 * altura)
                return(eer)

def carregamento():
    for i in range(2):
        for pontos in range(4):
            print(f"\rCarregando{'.' * pontos}   ", end='', flush=True)
            sleep(0.3)
    print("\rCarregado!     ")

def relatorio_dados_iniciais():
    print(f'{' DADOS INICIAIS ':-^60}')
    print(f'Nome: {nome}')
    print(f'Sexo: {'Masculino' if sexo == 'M' else 'Feminino'}')
    if idade >= 3:
        print(f'Idade: {idade:.0f} anos')
    else:
        print(f'Idade: {meses} meses')    
    print(f'Altura: {altura}cm / {altura/100:.2f}m')
    print(f'Peso: {peso:.1f}kg')
    if idade >= 3:
        print(f'Nivel de At. Física: {fatoratv}')

def relatorio_primario():
    print('-'*60)
    print(f'/ '*9,' Relatório Primário ','/ '*9)
    print(f'Nome: {nome}')
    print(f'Sexo: {'Masculino' if sexo == 'M' else 'Feminino'}')
    if idade >= 3:
        print(f'Idade: {idade:.0f} anos')
    else:
        print(f'Idade: {meses} meses')
    print(f'Altura: {altura}cm / {altura/100:.2f}m')
    print(f'Peso: {peso:.1f}kg')
    if idade >= 3:
        print(f'Nivel de At. Física: {fatoratv}')
    print('-'*60)
    print(f'O seu Índice de massa corporal é de {imc:.2f}kg/m², o que indica \nque você no momento está em {estado}.')
    print(f'O EER calculado é de {eer:.2f} kcal por dia.')

def relatorio_final():
    print(f'{' RELATÓRIO FINAL ':=^60}')
    relatorio_dados_iniciais()

    print('-'*60)
    print(f'O seu Índice de massa corporal é de {imc:.2f}kg/m², o que indica \nque você no momento está em {estado}.')
    print(f'O EER calculado é de {eer:.2f} kcal por dia.')
    if idade >= 3:
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
    idade = float(input('Qual a sua idade? '))

    if idade < 3:
        meses = verificador_bebe(idade)
        idade_crianca = conversao_idade(meses)

    peso = float(input('Digite seu peso em kg: '))
    altura = int(input('Digite sua altura em centimetros: '))

    imc = calcular_imc(peso, altura)
    estado = verificacao_imc(imc)

    if idade >= 3:
        # FATOR ATIVIDADE
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
        eer = calcular_eer2(sexo, idade, peso, altura, fatoratv)
    else:
        eer = calcular_eer_crianca(idade_crianca)

    if idade >= 3:
        relatorio_primario()
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
            
    relatorio_final()

    continuar = 'nulo'
    while continuar not in ('S', 'N'):
        continuar = str(input('Deseja fazer outro cálculo? [S/N] ')).upper().strip()[0]
        if continuar not in ('S', 'N'):
            print('Resposta inválida. Tente outra vez!')
    if continuar == 'N':
        break
    else:
        carregamento()
print('='*60)
print(f'{' PROGRAMA ENCERRADO ':/^60}')
