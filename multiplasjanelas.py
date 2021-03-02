import PySimpleGUI as sg 

def janela_id():
    sg.theme("Dark")

    coluna = [
        [sg.Button("Entrar")]
    ]

    layout = [
        [sg.Text("Nome do aluno:"), sg.Input(key="aluno", size=(15,0))],
        [sg.Column(coluna, justification="center")]
    ]

    return(sg.Window("EduCalc", layout=layout, finalize=True))

def janela_aluno():
    sg.theme("Dark")
    
    layout = [
        [sg.Text("Média 1:"), sg.Input(key="m1", size=(15,0))],
        [sg.Text("Média 2:"), sg.Input(key="m2", size=(15,0))],
        [sg.Button("Voltar"), sg.Button("Resultado")],
        [sg.Print()]
    ]

    return(sg.Window("EduCalc - Situação", layout=layout, finalize=True))

janela1, janela2 = janela_id(), None

while True:
    window, event, values = sg.read_all_windows()
    if window == janela1 and event == sg.WIN_CLOSED:
        break
    if window == janela2 and event == sg.WIN_CLOSED:
        break
    if window == janela1 and event == "Entrar":
        nome = values["aluno"]
        janela1.hide()
        janela2 = janela_aluno()
    if window == janela2 and event == "Voltar":
        janela2.hide()
        janela1.UnHide()
    elif window == janela2 and event == "Resultado":
        media = (int (values["m1"]) + int (values["m2"])) / 2
        if media < 7:
            sg.popup("Nome do Aluno: ", nome, "Média: ", media, "Aluno na recuperação final.")
        else:
            sg.popup("Nome do Aluno: ", nome, "Média: ", media, "Aluno aprovado!")  