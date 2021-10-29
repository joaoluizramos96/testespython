from rich import print
from rich.progress import track
from time import sleep
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt

cpf = 0
conf = 0
opc = 0

prompt = Prompt()
console = Console()
table = Table(title="DJHOW TELECOM\n")

table.add_column("Plano", style="bold green")
table.add_column("Velocidade", style="bold blue")
table.add_column("Valor", style="bold yellow")

table.add_row("Básico", "100 Mbps", "R$ 50,00")
table.add_row("Premium", "250 Mbps", "R$ 80,00")
table.add_row("Master", "1 Gbps", "R$ 150,00")

while conf == 0:
	cpf = int(input("Informe o número do seu CPF: "))
	conf = prompt.ask (f'CPF informado: [on black]{cpf}[/]. Correto (1-sim/0-não)?')

for i in track(range(10), "Aguarde enquanto buscamos seu CPF no sistema..."):
	sleep(1)
print (" ")
print (":white_check_mark: Análise finalizada!")
print (" ")
console.log(table)
