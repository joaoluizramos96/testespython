import  PySimpleGUI as sg

class TelaPython():    
    def __init__(self):
        # Layout
        sg.change_look_and_feel("Black")
        layout = [
            [sg.Text("Nome:", size=(5,0)), sg.Input(size=(15,0), key="nome")],
            [sg.Text("Idade:", size=(5,0)), sg.Input(size=(15,0), key="idade")],
            [sg.Text("Quais provedores de e-mail são aceitos?")],
            [sg.Checkbox("Gmail", key="gmail"), sg.Checkbox("Outlook", key="outlook"), sg.Checkbox("Yahoo!", key="yahoo")],
            [sg.Text("Aceita Cartão?")],
            [sg.Radio("Sim", "cartoes", key="aceitaCartao"), sg.Radio("Não", "cartoes", key="naoAceitaCartao")],
            [sg.Button("Enviar Dados")],
            [sg.Output(size=(30, 10))]
        ]
        # Janela
        self.janela = sg.Window("Dados do Usuário").layout(layout)


    def Iniciar(self):
        while True:
            # Extrair os dados da tela
            self.button, self.values = self.janela.Read()
            nome = self.values["nome"]
            idade = self.values["idade"]
            aceita_gmail = self.values["gmail"]
            aceita_outlook = self.values["outlook"]
            aceita_yahoo = self.values["yahoo"]
            aceita_cartao = self.values["aceitaCartao"]
            print(f"Nome: {nome}")
            print(f"Idade: {idade}")
            print(f"Gmail? {aceita_gmail}")
            print(f"Outlook? {aceita_outlook}")
            print(f"Yahoo? {aceita_yahoo}")
            print(f"Aceita cartão? {aceita_cartao}")
            print("----------------------------------------")

tela = TelaPython()
tela.Iniciar()
