# Bibliotecas importadas
import os
from datetime import datetime, date
import locale
import sqlite3 as sqlite

# Criando conexão com o banco (se não existente, cria o banco)
conexao = sqlite.connect("loja.db")

# Criando a conexão para execução de queries
cursor = conexao.cursor()

# Setando como UTF-8 pra todas as categorias 
locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")

def inserirDadosPedido():
    # Limpando o console pra melhor visualização
    os.system("cls")
    
    quantidadeRegistros = int(input("Quantos pedidos serão registrados?"))
    
    for i in range(quantidadeRegistros):

        # Criando variáveis de input
        numNotaFiscal = int(input("Digite o número da nota fiscal\n"))
        valorTotal = round(float(input("Digite o valor total do produto\n")), 2)

        # Primeira forma de adicionar a data do pedido (pegando automaticamente)
        dataPedido = date.today().strftime("%d/%m/%Y")
        
        # Usar pra fazer query verificando se o cliente existe
        cpfCliente = input("Qual o CPF do cliente que efetuou a compra (sem traços e pontos)\n")
        
        # Verificando se o id existe
        sql = """
            SELECT IDCLIENTE FROM CLIENTES WHERE CPF = ?;
        """
        
        
        
    return 0


inserirDadosPedido()


    # Segunda forma de adicionar a data do pedido (usuário inputando)
    # # Usando desta forma, pedir para o usuário digitar o dia, mês e ano no formato dd/mm/yyyy e fazer verificação se ele digitou assim usando o strftime talvez
    