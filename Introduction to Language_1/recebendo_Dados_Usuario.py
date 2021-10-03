"""
Recebendo dados do usuario

input() -> Todo dado recebido via input é do tipo String

Em pytho, String é tudo que estiver entre:

- Aspas simples;
- Aspas duplas;
- Aspas simples triplas;
- Aspas duplas triplas;

Exemplos:

- Aspas simples -> 'angelina Jolie'
- Aspas duplas -> "angelina Jolie"
- Aspas simples -> '''angelina Jolie'''
"""
# Aspas duplas triplas -> """angelina Jolie"""
# Entrada de Dados
#print("Qual seu nome?")


"""
nome = input()  # input -> Entrada de dados

O input é um recurso integrado do Python, 
no qual faz parte das *builtins*
Built-in Objects (Objetos Integrados)

"""

nome = input("Qual seu nome?")


# EXEMPLO DE PRINT 'ANTIGO 2.X'
# print('Seja Bem-vindo(a) %s' % nome)

# EXEMPLO DE PRINT 'MAIS ATUAL' 3.7
print(f'Seja bem-vindo(a) {nome}')

# print("Qual sua idade?")
# idade = input()
idade = int(input('Qual sua idade?'))


# Processamento
# Saída de dados
# print('A %s tem %s anos' % (nome, idade))

# EXEMPLO DE PRINT 'MODERNO' 3.x
# print('Seja Bem-Vindo(a){0}'.format(nome))
# print('A {0} tem {1} anos' .format(nome, idade))

# EXEMPLO DE PRINT 'MAIS ATUAL' 3.7
print(f'A {nome} tem {idade} anos')

"""
# int(idade) => cast
Cast é a 'conversão' de um tipo de dado para outro
"""
print(f'A {nome} nasceu em {2019-int(idade)}'
)