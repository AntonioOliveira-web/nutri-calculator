# main.py

from calculos import (
    calcular_imc,
    conversao_idade,
    calcular_eer_crianca,
    calcular_eer2
)

from classificacoes import verificacao_imc

from entradas import (
    verificador_bebe,
    escolher_fator_atividade
)

from relatorios import (
    relatorio_final,
    orientação,
    carregamento
)

while True:
    print('-='*30)
    print(f'{' CALCULADORA NUTRICIONAL ':-^60}')
    print('-='*30)

    # 1. Receber dados gerais
    nome = str(input('Digite o seu nome: ')).strip().title()
    sexo = str(input('Qual seu sexo? [M/F] ')).strip().upper()[0]
    idade = float(input('Qual a sua idade? '))
    # Inicialização das variáveis
    meses = None
    idade_crianca = None
    fatoratv = None

    # 2. Verificação de faixa etária
    if idade < 3:
        meses = verificador_bebe(idade)
        idade_crianca = conversao_idade(meses)

    # 3. Recebimento do peso e altura
    peso = float(input('Digite seu peso em kg: '))
    altura = int(input('Digite sua altura em centimetros: '))

    # 4. Calcular IMC
    imc = calcular_imc(peso, altura)
    estado = verificacao_imc(imc)

    # 5. Calcular EER
    if idade >= 3:
        fatoratv = escolher_fator_atividade()
        eer = calcular_eer2(sexo, idade, peso, altura, fatoratv)
    else:
        eer = calcular_eer_crianca(idade_crianca, sexo, altura, peso)

    # 6. Apresentar dados
    relatorio_final(nome, sexo, idade, meses, peso, altura, fatoratv, imc, estado, eer)

    # 7. Perguntar se deseja continuar
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
