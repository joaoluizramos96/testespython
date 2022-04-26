from faker import Faker

fake = Faker()

nome = fake.name()
primeiroNomeFeminino = fake.first_name_female()
usuario = fake.user_name()
senha = fake.password(20)
mes = fake.month()

print("Nome:", nome)
print("Primeiro nome feminino:", primeiroNomeFeminino)
print("Usuário:", usuario)
print("Senha:", senha)
print("Mês:", mes)
