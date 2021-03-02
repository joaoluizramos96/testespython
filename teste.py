import PySimpleGUI as sg

class TelaPython():
    def __init__(self):

        sg.theme("Black")

        layout_column = [
            [sg.Text("\nBem-vindo(a)!\n", font="Comic")],
            [sg.Text("Login", font=("Comic", 10))],
            [sg.Text("E-mail:"), sg.Input(key="email",size=(21,0))],
            [sg.Text("Senha:"), sg.InputText(key="senha",password_char="*", size=(21,0))],
            [sg.Button("Entrar")]
            #[sg.Output(size=(33,10))],
        ]

        footer = [
            [sg.Text("Desenvolvido por: João Luiz™ - 2021", text_color="gray", font=('Comic', 6))]
        ]

        layout = [
            [sg.Column(layout_column, element_justification='center')],
            [sg.Column(footer, justification="right")]
        ]

        self.janela = sg.Window("Login e Senha - Teste").layout(layout)

    def IniciarTela(self):
        while True:
            self.Button, self.values = self.janela.Read()
            e = self.values["email"]
            s = self.values["senha"]

            if (e == "admin@admin.com" and s == "123"):
                sg.PopupOK("Login realizado com sucesso!!")
            else:
                sg.PopupError("Senha incorreta. Tente novamente.")


inicio = TelaPython()
inicio.IniciarTela()
