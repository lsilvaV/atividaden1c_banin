import os
from datetime import datetime, date
import locale

locale.setlocale(locale.LC_TIME, )
def inserirDadosPedido():
    os.system("cls")
    # Criando variáveis de input
    numNotaFiscal = int(input("Digite o número da nota fiscal"))
    valorTotal = round(float(input("Digite o valor total do produto")), 2)

    # Primeira forma de adicionar a data do pedido (pegando automaticamente)
    date.today().strftime("%d/%m/%Y")
    # Segunda forma de adicionar a data do pedido (usuário inputando)
    # # Usando desta forma, pedir para o usuário digitar o dia, mês e ano no formato dd/mm/yyyy e fazer verificação se ele digitou assim usando o strftime talvez
    
    

    return 0
inserirDadosPedido()