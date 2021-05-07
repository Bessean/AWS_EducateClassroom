#Objetivo
#Inserir dados de arquivos .csv em um banco de dados relacional.
#Extrair dados de um banco de dados relacional e gravar no formato .csv.

#Conexão com banco de dados relacional
#Criando uma engine com o banco de dados.
import sqlalchemy, pandas as pd,pyodbc
server = 'sql20211.cp1ri5jswsct.us-east-1.rds.amazonaws.com'  
database = 'GRUPOC' 
username = 'aaa'
password = 'xxx' 
con1 = f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC Driver 17 for SQL Server"
engine = sqlalchemy.create_engine(con1)
engine.connect()

#Criando um dataframe para cada arquivo
df_aluno = pd.read_csv(filepath_or_buffer = '/content/ALUNO.csv',delimiter=';',encoding = 'ISO-8859-1')
df_convidado = pd.read_csv(filepath_or_buffer = '/content/CONVIDADO.csv',delimiter=';',encoding = 'ISO-8859-1')
df_fregues = pd.read_csv(filepath_or_buffer = '/content/FREGUES.csv',delimiter=';',encoding = 'ISO-8859-1')
df_funcionario = pd.read_csv(filepath_or_buffer = '/content/FUNCIONARIO.csv',delimiter=';',encoding = 'ISO-8859-1')
df_imovel = pd.read_csv(filepath_or_buffer = '/content/IMOVEL.csv',delimiter=';',encoding = 'ISO-8859-1')

#Inserindo todos os arquivos no banco de dados, utilizando o comando “to_sql”.
df_aluno.to_sql(("aluno"),engine,if_exists = "replace")
df_convidado.to_sql(("convidado"),engine,if_exists = "replace")
df_fregues.to_sql(("fregues"),engine,if_exists = "replace")
df_funcionario.to_sql(("funcionario"),engine,if_exists = "replace")
df_imovel.to_sql(("imovel"),engine,if_exists = "replace")

#criar um dataframe para ler os arquivos
df_informacao = pd.read_sql(sql ="SELECT * FROM INFORMACAO",con=engine2)
df_informacao.to_csv(("informação_ac2.csv"),index=False, line_terminator='\n')
