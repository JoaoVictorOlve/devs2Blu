import psycopg2

try:
    conn = psycopg2.connect(host = "localhost", port = "5437", database = "postgres", user = "teste", password ="123456")
    print("Conectou")
except:
    print('Falhou')

if conn is not None:
    print("Tá estável")
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE JOAO (id int not null generated always as identity, nome varchar(30), sobrenome varchar(50))')
    conn.commit()

    cursor.close()
    conn.close()