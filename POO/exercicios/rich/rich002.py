from rich import print
from rich.panel import Panel

caixa = Panel("[white] Iphone \n ""---------------" "\n ........Preco: 25.000........" ".", justify="center", title="Produto", style="red", expand=False)


print(caixa)