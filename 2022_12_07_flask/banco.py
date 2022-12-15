import psycopg2

try:
    conn = psycopg2.connect(host = "localhost",
    port = "5435",
    database = "postgres",
    user = "teste",
    password = "123456")
    print("Conectado")
except:
    print("Desconectado")

if conn != None:
    print("Conexão estável")
    
    cursor = conn.cursor()

    cursor.execute('CREATE TABLE usuarios  (nome VARCHAR(15) NOT NULL, nickname VARCHAR(30)NOT NULL, senha VARCHAR(30)NOT NULL,  PRIMARY KEY(nickname) );')

    cursor.execute('CREATE TABLE funcionarios  (id serial, nome VARCHAR(15) NOT NULL, idade INT NOT NULL, altura FLOAT NOT NULL, PRIMARY KEY(id));')

    conn.commit()
    cursor.close()
    conn.close()