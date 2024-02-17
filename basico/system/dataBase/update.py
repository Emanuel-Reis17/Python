import mysql.connector

mydb = mysql.connector.connect(
    host = 'Localhost', 
    user = 'root', 
    password = '1234', 
    database = 'python'
)

mycursor = mydb.cursor()

cidade = 'Rio de Janeiro'
idCliente = 2

# Atualizando a tabela
print('Atualizando a tabela...')
sql = "UPDATE cliente SET Cidade = %s WHERE IdCliente = %s"
val = (cidade, idCliente)
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, ' record(s) updated')
