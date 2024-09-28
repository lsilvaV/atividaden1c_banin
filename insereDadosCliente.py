import sqlite3 as sqlite

conexao = sqlite.connect("loja.db")
cursor = conexao.cursor()

cpf = input("Digite o seu CPF: ")
rg = input("Digite o seu RG (opcional): ")
endereco = input("Digite o seu endereco: ")
email = input("Digite o seu email: ")
telfixo = input("Digite o seu telefone fixo (opcional): ")
celular = input("Digite o seu número de celular: ")

# Query SQL para inserir os dados
sql = """
INSERT INTO cliente (cpf, rg, endereco, email, telefonefixo, celular)
VALUES (?, ?, ?, ?, ?, ?)
"""

# Executa a query com os dados do usuário
cursor.execute(sql, (cpf, rg, endereco, email, telfixo, celular))

# Confirma as mudanças
conexao.commit()

# Feche a conexão
conexao.close()
