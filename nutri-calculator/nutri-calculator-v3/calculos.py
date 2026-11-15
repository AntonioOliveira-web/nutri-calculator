# calculos.py

def calcular_imc(peso, altura):
    imc = peso / ((altura / 100) ** 2)
    return(imc)

def conversao_idade(meses):
    idade_crianca = meses / 12 
    return idade_crianca

def calcular_eer_crianca(idade_crianca, sexo, altura, peso):
    if 0 <= idade_crianca < 0.25:
        # GRUPO DE 0 MESES À 2.99 MESES
        if sexo == 'M':
            eer = -716.45 - (1.00 * idade_crianca) + (17.82 * altura) + (15.06 * peso) + 200
        else:
            eer = -69.15 - (80.00 * idade_crianca) + (2.65 * altura) + (56.15 * peso) + 180
        
    elif 0.25 <= idade_crianca < 0.5:
        # GRUPO DE 3 MESES À 5.99 MESES
        if sexo == 'M':
            eer = -716.45 - (1.00 * idade_crianca) + (17.82 * altura) + (15.06 * peso) + 50
        else:
            eer = -69.15 + (80.00 * idade_crianca) + (2.65 * altura) + (54.15 * peso) + 60        
        
    elif 0.5 <= idade_crianca < 3:
        # GRUPO DE 6 MESES À 2.99 ANOS
        if sexo == 'M':
            eer = -716.45 - (1.00 * idade_crianca) + (17.82 * altura) + (15.06 * peso) + 20
        else:
            eer = -69.15 + (80.00 * idade_crianca) + (2.65 * altura) + (54.15 * peso) + (20 if 0.5 <= idade_crianca < 1.0 else  15)
    return eer

def calcular_eer2(sexo, idade, peso, altura, fatoratv):

    if 3 <= idade < 14:
        # GRUPO DE CRIANÇAS DE 3 À 13.99 ANOS
        if sexo == 'M':
            # FÓRMULA MASCULINA
            if fatoratv == 'Sedentário':
                eer = -447.51 + (3.68 * idade) + (13.01 * altura) + (13.15 * peso) + (20 if 3 <= idade < 4 else 15 if 4 <= idade < 9 else 25)
            elif fatoratv == 'Pouco Ativo':
                eer = 19.12 + (3.68 * idade) + (8.62 * altura) + (20.28 * peso) + (20 if 3 <= idade < 4 else 15 if 4 <= idade < 9 else 25)
            elif fatoratv == 'Ativo':
                eer = -388.19 + (3.68 * idade) + (12.66 * altura) + (20.46 * peso) + (20 if 3 <= idade < 4 else 15 if 4 <= idade < 9 else 25)
            else:
                eer = -671.75 + (3.68 * idade) + (15.68 * altura) + (23.25 * peso) + (20 if 3 <= idade < 4 else 15 if 4 <= idade < 9 else 25)
        else:
            # FÓRMULA FEMININA
            if fatoratv == 'Sedentário':
                eer = 55.69 - (22.25 * idade) + (8.43 * altura) + (17.07 * peso) + (15 if 3 <= idade < 4 else 15 if 4 <= idade < 9 else 30)
            elif fatoratv == 'Pouco Ativo':
                eer = -297.54 - (22.25 * idade) + (12.77 * altura) + (14.73 * peso) + (15 if 3 <= idade < 4 else 15 if 4 <= idade < 9 else 30)
            elif fatoratv == 'Ativo':
                eer = -189.55 - (22.25 * idade) + (11.74 * altura) + (18.34 * peso) + (15 if 3 <= idade < 4 else 15 if 4 <= idade < 9 else 30)
            else:
                eer = -709.59 - (22.25 * idade) + (18.22 * altura) + (14.25 * peso) + (15 if 3 <= idade < 4 else 15 if 4 <= idade < 9 else 30)
     
    elif 14 <= idade < 19:
        # GRUPO DE ADOLECENTES DE 14 À 18.99 ANOS
        if sexo == 'M':
            # FÓRMULA MASCULINA
            if fatoratv == 'Sedentário':
                eer = -447.51 + (3.68 * idade) + (13.01 * altura) + (13.15 * peso) + 20
            elif fatoratv == 'Pouco Ativo':
                eer = 19.12 + (3.68 * idade) + (8.62 * altura) + (20.28 * peso) + 20
            elif fatoratv == 'Ativo':
                eer = -388.19 + (3.68 * idade) + (12.66 * altura) + (20.46 * peso) + 20
            else:
                eer = -671.75 + (3.68 * idade) + (15.68 * altura) + (23.25 * peso) + 20
        else:
            # FÓRMULA FEMININA
            if fatoratv == 'Sedentário':
                eer = 55.69 - (22.25 * idade) + (8.43 * altura) + (17.07 * peso) + 20
            elif fatoratv == 'Pouco Ativo':
                eer = -297.54 - (22.25 * idade) + (12.77 * altura) + (14.73 * peso) + 20
            elif fatoratv == 'Ativo':
                eer = -189.55 - (22.25 * idade) + (11.74 * altura) + (18.34 * peso) + 20
            else:
                eer = -709.59 - (22.25 * idade) + (18.22 * altura) + (14.25 * peso) + 20

    else: # if idade >= 19:
        # GRUPO DE ADULTOS *ACIMA* DE 18 ANOS
        if sexo == 'M':
            # FÓRMULA MASCULINA
            if fatoratv == 'Sedentário':
                eer = 753.07 - (10.83 * idade) + (14.10 * peso) + (6.50 * altura)
            elif fatoratv == 'Pouco Ativo':
                eer = 581.47 - (10.83 * idade) + (14.94 * peso) + (8.30 * altura)
            elif fatoratv == 'Ativo':
                eer = 1004.82 - (10.83 * idade) + (15.91 * peso) + (6.52 * altura)
            else:
                eer = -517.88 - (10.83 * idade) + (19.11 * peso) + (15.61 * altura)
    
        else:
            # FÓRMULA FEMININA
            if fatoratv == 'Sedentário':
                eer = 584.90 - (7.01 * idade) + (11.71 * peso) + (5.72 * altura)
            elif fatoratv == 'Pouco Ativo':
                eer = 575.77 - (7.01 * idade) + (12.14 * peso) + (6.60 * altura)
            elif fatoratv == 'Ativo':
                eer = 710.25 - (7.01 * idade) + (12.34 * peso) + (6.54 * altura)
            else:
                eer = 511.83 - (7.01 * idade) + (12.56 * peso) + (9.07 * altura)
    return eer
