import mysql.connector

banco = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "cdd2022",
    database = "escola_turma_b"
)
print(banco)

meucursor = banco.cursor()
pesquisa = 'select * from alunos;'
meucursor.execute(pesquisa)
#fetchall recebe tudo da pesquisa e retorna através de uma tupla
resultado = meucursor.fetchall()
for x in resultado:
    print(x)
#meucursor.close()
#banco.close()

nome1 = "fernanda"
cpf1 = "82340698667"
telefone1 = "92258852"
media1 = 8.2
fk_turmas1 = 2
cursor = banco.cursor()
sql = "INSERT INTO alunos (nome, CPF, telefone, media, fk_turmas) VALUES (%s,%s,%s,%s,%s)"
data = (nome1, cpf1, telefone1, media1, fk_turmas1)
cursor.execute(sql,data)
banco.commit()
userid = cursor.lastrowid
print(userid)
cursor.close()
banco.close()