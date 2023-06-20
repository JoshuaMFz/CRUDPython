"""
Criada pela IBM:
Padronizada: ANSI e ISO

MYSQL, SQL Server, Oracle, PostGreSQL, MariaDB, SQLITE, SyBase, Informix, Microsoft Access

inserir, excluir, alterar, visualizar, ordenar, juntar, mesclar, intercalar, criar tabela, alterar tabela
remover tabela, alterar estruturas de dados nos campos da tabela, etc...

Divido em três partes: LDD, LCD, LMD

(LDD)
Linguagem de Definição de Dados
Comandos: create, drop, alter

(LMD)
Linguagem de Manipulação de Dados
Select, Update, Insert, Delete.

(LCD):
Linguagem de Controle de Dados:

Permissões de Acesso
Grant, Revoke

Data Types: Dados Padrões.
Primitivos: integer, char, long, float, datetime, binary


Consulta:

SELECT clientes.id, clientes.nome, clientes.email
FROM clientes
WHERE clientes.situacao = 'INATIVO'
    ORDER BY clientes.nome

Adição:

INSERT INTO clientes (nome, email, situacao)
VALUES ('Joshua Martins', 'joshuak6k@gmail.com', 'ATIVO')

Atualização:

UPDATE clientes
SET situacao = 'INATIVO'
WHERE id BETWEEN 1 and 30

Remoção:

DELETE FROM clientes
WHERE id = idusuario

JOIN

SELECT clientes.nome, pedidos.id, pedidos.data
FROM pedidos
INNER JOIN clientes ON clientes.id = pedidos.id
    AND clientes.id = 27

ALTER JOIN
LEFT JOIN
RIGHT JOIN

"""