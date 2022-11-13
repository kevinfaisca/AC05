import pyodbc

dados_conexao = (
    "Driver={SQL Server};"
    "Server=KEVINFAISCA\SQLEXPRESS;"
    "Database=estudo;"
)

conexao = pyodbc.connect(dados_conexao)
print("conexao bem sucedida")

cursor = conexao.cursor()

COD_DEPTO = 4
NOME = "Carlos Alberto"
CPF = 28447444886
SALARIO = 6000
TELEFONE = 6622788647292
RG = 119982227
BAIRRO = "ALPHAVILLE"
CIDADE = "BARUERI"
UF = "SP"
CEP = "08561424"


comando =   f"""INSERT INTO TB_FUNCIONARIO (COD_DEPTO,NOME,CPF,SALARIO,TELEFONE,RG, BAIRRO, CIDADE, UF, CEP) 
                VALUES 
                ({COD_DEPTO},'{NOME}',{CPF},{SALARIO},{TELEFONE},{RG},'{BAIRRO}','{CIDADE}','{UF}','{CEP}')"""

cursor.execute(comando)
cursor.commit()

#Atualizar dados

conexao = pyodbc.connect(dados_conexao)
cursor = conexao.cursor()

cursor.execute("""
UPDATE TB_FUNCIONARIO
SET NOME = 'Kevin'
WHERE IDFUNCIONARIO = 19;
""")

conexao.commit()
  


#Deletar dados

cursor.execute("""
DELETE FROM TB_FUNCIONARIO
WHERE IDFUNCIONARIO =25;
""")
conexao.commit()
