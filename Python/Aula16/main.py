from database import db
from tabulate import tabulate
#https://dontpad.com/216-16-09

cursor = db.cursor()
#cursor do meu banco de dados
query = 'SELECT * FROM aluno;'
cursor.execute(query)
#Executando 
res = cursor.fetchall()

for linha in res:
    print(tabulate(linha))

cursor.close()
db.commit()
db.close()