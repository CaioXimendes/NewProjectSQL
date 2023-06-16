import mysql.connector

banco = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "cdd2022",
    database = "escola_turma_b"
)
print(banco)

cursor = banco.cursor()
sql = "DELETE FROM alunos where matricula = 9"
cursor.execute(sql)
banco.commit()
cursor.close()
banco.close()