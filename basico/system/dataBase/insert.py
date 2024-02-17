import mysql.connector

mydb = mysql.connector.connect(
    host = 'Localhost', 
    user = 'root', 
    password = '1234', 
    database = 'python'
)

mycursor = mydb.cursor()

cliente = 'Jessica'
telefone = '876453488'
cidade = 'São Paulo'

# Inserindo a tabela
print('Inserindo a tabela...')
sql = "INSERT INTO cliente (Nome, Telefone, Cidade) VALUES (%s, %s, %s)"
val =  (cliente, telefone, cidade)
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, ' record(s) inserted')
