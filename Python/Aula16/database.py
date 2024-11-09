import mysql.connector as mysql


try:
  db = mysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='In@12345678',
    database='ESCOLA'
)

except:
  print("\033[31m Erro ao conectar ao banco de dados. Por favor tente novamente\033[m")

else:
  print("\033[32mConexão com o banco estabelecida com sucesso \033[m!")

# resultado = cursor.fetchall()

