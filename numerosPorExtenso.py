from num2words import num2words

numero = int(input("Digite um número: "))

num_en = num2words(numero, lang="en")
print(f"Em Inglês: {num_en}")

num_en_ord = num2words(numero, lang="en", to="ordinal")
print(f"Em Inglês (ordinal): {num_en_ord}")

num_pt = num2words(numero, lang="pt-br")
print(f"Em Português: {num_pt}")

num_pt_ord = num2words(numero, lang="pt-br", to="ordinal")
print(f"Em Português (ordinal): {num_pt_ord}")
