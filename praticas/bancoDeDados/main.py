import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", 
    user="root", 
    password="", 
    database="pythonsql"
)

mycursor = mydb.cursor()
mycursor.execute("INSERT INTO vendas (id_venda, cliente, produto, 0000-00-00, )")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
