import mysql.connector

mydb = mysql.connector.connect(
    host = 'Localhost', 
    user = 'root', 
    password = '1234', 
    database = 'python'
)

mycursor = mydb.cursor()

# Deletando a tabela
print('Deletando a tabela...')
sql = 'DELETE FROM cliente WHERE IdCliente = \'5\''
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, ' record(s) deleted')
