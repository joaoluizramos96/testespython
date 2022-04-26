import random

milhares = [] #Lista de armazenamento das milhares
qnt = 0 # Quantidade de milhares armazenadas
cont = 0 # Contador para "varrer" a lista ao apresentar as milhares
bilhete = 1 # Quantidade de bilhetes a serem gerados
lacoWhile = 0
lacoGerarBilhete = 0
m1 = 0
m2 = 1
m3 = 2
m4 = 3

solic = int(input("Deseja gerar quantos bilhetes? ")) # Solicitacao de quantos bilhetes serao gerados (cada bilhete gera 4 milhares)

#Gerando numeros aleatorios (em inteiro)
while lacoWhile < solic:
  while lacoGerarBilhete < 4:
    m = random.randint(0,9)
    c = random.randint(0,9)
    d = random.randint(0,9)
    u = random.randint(0,9)
    #Convertendo int para strings (concatena-las)
    M = str(m)
    C = str(c)
    D = str(d)
    U = str(u)
    #Contatenando os numeros
    milhar = M+C+D+U
    #Jogando a concatenacao na lista e incrementando a posicao para adicionar em um campo vazio 
    milhares.append(milhar)
    qnt = qnt + 1
    lacoGerarBilhete = lacoGerarBilhete + 1
  lacoWhile = lacoWhile + 1

lacoWhile = 0
lacoGerarBilhete = 0

# Estrutura de repeticao para apresentar as milhares
if solic != 0:
  print ("-------------------------------------")
  while (cont < solic):
    print("Bilhete", bilhete)
    print(milhares[m1], milhares[m2], milhares[m3], milhares[m4])
    m1 = m1 + 4
    m2 = m2 + 4
    m3 = m3 + 4
    m4 = m4 + 4
    cont = cont + 1
    bilhete = bilhete + 1
print ("-------------------------------------")
