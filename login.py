opc = 1
login = []
senha = []
arquivo = open("/home/joao/brincando_com_python/login_senha.txt", "wt")

def menu():
    print ('''\nEscolha uma opção:\n
        [1] Criar cadastro;
        [2] Realizar autenticação;
        [0] Sair;\n''')
    return()

menu()

def criar_login():
    qnt_l = 0
    qnt_s = 0
    l = str(input("Informe o login a ser cadastrado: "))
    arquivo.write(l)
    login.append(qnt_l)
    qnt_l = qnt_l + 1
    s = str (input("Informe a senha a ser cadastrada: "))
    arquivo.write(s)
    senha.append(qnt_s)
    qnt_s = qnt_s + 1