from num2words import num2words

anoDeNascimento = int(input("Informe seu ano de nascimento (ex.: 1980): "))
conf = str(input("Já fez aniversário esse ano (1-sim/2-não)? "))
idade = 0

if (conf == "1"):
  idade = 2022 - (anoDeNascimento)
else:
  idade = 2021 - (anoDeNascimento)

print ("\n")
print("Sua idade: ", idade)
