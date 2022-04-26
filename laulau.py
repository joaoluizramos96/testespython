import random
import math
import statistics



continu = 1

while continu == 1:

    print('       Menu       ')
    print(
        'Escolha A operação que você quer estudar.\n digite (1) para media aritmetica \n digite (2) para divisão \n '
        'digite (3) para '
        'multiplicação\n')
    operacao = input('Digite: ')
        # Esse while ele esta validando o input que o usuario fornece se for string ele não aprova
    while not operacao.isdigit():
        print('Digite apenas o numero com a função correspondente:')
        operacao = input()
        # A variavel operacao esta sendo transformada em int
    operacao = int(operacao)

    if operacao == 1:
        print('Você escolheu a operação de media aritmetica\n ')
            # Variaveis criadas com a biblioteca  random para criar numeros aleatorios cada vez que o programa for iniciar.
        num1 = random.randint(10, 100)
        num2 = random.randint(10, 100)
        num3 = random.randint(10,100)
        # Statistics.nean é da biblioteca statistics. Ela faz a media aritimetica das variaveis.
        res = statistics.mean([num1, num2, num3])
            # round pertence a biblioteca math, ele arredonda um numero float para apenas um numero inteiro e  duas casas deciamais.
        res=round(res,2)

        print(f'O valor da conta de telefone de Sebastião variou muito nos três primeiros meses de 2012. Em janeiro, \n'
              f'Sebastião pagou R$ {num1:.2f}  em fevereiro, R$ {num2:.2f} e em março, R$ {num3:.2f}. Qual foi, \n'
              f'em reais, o valor mensal médio da conta telefônica de Sebastião no primeiro trimestre de 2012?\n')

        #print(res)
        resu = int(input('resposta:'))
            # While para validação caso a resposta esteja errada.
        while resu != res:
            resu = int(input('Você errou, tente novamente:'))

        if resu == res:
            print('parabens vc acertou!\n')

    if operacao == 2:
        print('Você escolheu a operação de divisão\n ')

        num1 = random.randint(50, 100)
        num2 = random.randint(3, 10)
        # math.floor arredonda o numero o proximo mais baixo inteiro
        res = math.floor(num1 / num2)

        print(
            'Para realizar um campeonato de vôlei em uma escola o professor de educação física decidiu dividir os ', num1,
            '\n alunos em grupos. Sabendo que cada equipe para esse esporte deve ser composta por\n', num2 ,'pessoas '
            'quantas equipes o professor conseguiu formar?')
        #print(res)
        resu = int(input('resposta:'))

        while resu != res:
            resu = int(input('Você errou, tente novamente:'))

        if resu == res:
            print('parabens vc acertou!\n')

    if operacao == 3:

        print('Você escolheu a operação de multiplicação\n ')
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        res = num2 * num1

        print('Um corretor de redações leva, em média,', num1,
              '  minutos para corrigir \numa redação. Se em uma determinada semana ele corrigiu', num2,
              ' redações, \n o tempo que ele levou para corrigir essas redações foi de:')
        #print(res)
        resu = int(input('resposta:'))

        while resu != res:
            resu = int(input('Você errou, tente novamente:\n'))

        if resu == res:
            print('parabens vc acertou!\n')

    continu = input('Deseja resolver mais uma? [1]Sim [2]Não: ')

    while not continu.isdigit():
        print('Digite apenas o numero com a função correspondente.')
        continu = input()

    continu = int(continu)
