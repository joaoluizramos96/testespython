from rich.progress import track
from time import sleep
from rich import print

print ("")
print ("[bold blue]Barra de progresso[/]")
print ("")
for tarefa in track(range(5),"Processando..."):
    sleep(1)

print ("")
print (":white_check_mark: Feito!")
print ("")
