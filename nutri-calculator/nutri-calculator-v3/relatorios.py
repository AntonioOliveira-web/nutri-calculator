# relatorios.py

def relatorio_dados_iniciais(nome, sexo, idade, meses, altura, peso, fatoratv):
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

def relatorio_final(nome, sexo, idade, meses, peso, altura, fatoratv, imc, estado, eer):
    print(f'{' RELATÓRIO FINAL ':=^60}')
    relatorio_dados_iniciais(nome, sexo, idade, meses, altura, peso, fatoratv)
    print('-'*60)
    print(f'O seu Índice de massa corporal é de {imc:.2f}kg/m², o que indica \nque você no momento está em {estado}.')
    print(f'O EER calculado é de {eer:.2f} kcal por dia.')
    print('-'*60)
    orientação(estado)
    print('='*60)

def orientação(resultado):
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

def carregamento():
    from time import sleep
    for i in range(2):
        for pontos in range(4):
            print(f"\rCarregando{'.' * pontos}   ", end='', flush=True)
            sleep(0.3)
    print("\rCarregado!     ")
    