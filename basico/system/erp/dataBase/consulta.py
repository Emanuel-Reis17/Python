import mysql.connector

mydb = mysql.connector.connect(
    host = 'Localhost', 
    user = 'root', 
    password = '1234', 
    database = 'python'
)

mycursor = mydb.cursor()

# Consultando a tabela
print('Consultando a tabela...')
mycursor.execute('SELECT * FROM cliente')
myresult = mycursor.fetchall()
for line in myresult:
    print('Line: ' + str(line))
