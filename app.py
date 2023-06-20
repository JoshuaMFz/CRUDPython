import sqlite3

con = sqlite3.connect('database.sqlite3')
cursor = con.cursor()

# SQL ( Structed query language)

# DEFINIR A TABELA

create_table_people_str = """ 
CREATE TABLE IF NOT EXISTS Pessoas (
    id INTEGER NOT NULL PRIMARY KEY,
    nome TEXT,
    idade INTEGER
);
"""

create_database = cursor.execute(create_table_people_str)

sql_query = """SELECT name FROM sqlite_master  
  WHERE type='table';"""

#  Mostrar tabelas
print("Tabelas")
print(cursor.execute(sql_query).fetchall())
print("-----------")


"""
Pessoas
 ------------
| 1 Pedro 12
| 2 Joao 34
| 3 Carlos 46
| 4 Daniel 23
| 5 Indio 19

"""

# Botar o menu para rodar infinito até alguem digitar 0
# Fazer um if para cada operação, e quando entrar no if , camar a função
# dentro do ler ter a opção de ler um ou todos
# dentro do update e do delete, pedir para informar id
# estudar os comandos sql insert, select, delete, where, update
# fazer funcionar o método ler um, delete, update
# colocar a opção pra parar o programa - segunda / terça

# colocar o programa no github - quarta

# instalar linux dual boot - quinta sexta

# até dia 23/06


from nob2.op import Pessoa
i = True
while i:
    pessoa = Pessoa('database.sqlite3')
    nome = int(input("""
    1) Criar
    2) Ler
    3) Atualizar
    4) Deletar
    5) Encerrar o Programa
    Sua opção: 
    """))
    if nome == 0:
        break
    elif nome == 1:
        print('Criar')
        nome_usuario = str(input('Digite seu nome: '))
        idade_usuario = int(input('Digite sua idade: '))
        pessoa.create(nome_usuario, idade_usuario)
        # create()
    elif nome == 2:
        print('Ler')
        # read()
        opcao = int(input('''Escolha a opção:
        1) Ler um
        2) Ler Todos'''))
        if opcao == 1:
            print('Lendo um!!')
            idusuario = input('Digite o ID: ')
            print(pessoa.read(idusuario))
        elif opcao == 2:
            print('Lendo Todos')
            print(pessoa.read_all())
        else:
            print('Opção Inválida')
    elif nome == 3:
        print('Atualizar')
        # update()
        idusuario = input('Digite o ID: ')
        nome = input('Digite o novo nome: ')
        idade = input('Digite a nova idade: ')

        print(pessoa.update(nome, idade, idusuario))
    elif nome == 4:
        print('Deletar')
        # delete()
        idusuario = input('Digite o ID: ')
        print(pessoa.delete(idusuario))

    elif nome == 5:
        print('Encerrando o programa!')
        i = False










