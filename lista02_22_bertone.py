'''
Nome: Bertone Porto
Data: 21/11/24

22. Crie um programa para um caixa
eletrônico que leia o valor solicitado
por um usuário
e imprima a menor quantidade possível
de notas a ser dada ao usuário.
Assume-se que
existam notas de 50, 20, 10, 5 e 1.
Imprimir também a quantidade de cada nota a ser
dada ao usuário.
Exemplo: 98 = uma nota de 50,
duas notas de 20, uma nota de 5,
e três notas de 1.
'''

valor = int(input("Digite o valor solicitado: "))

#variáveis para contagem de notas
notas50 = valor // 50
valor %= 50
notas20 = valor // 20
valor %= 20
notas10 = valor // 10
valor %= 10
notas5 = valor // 5
valor %= 5
notas1 = valor

#resultados
print("Menor quantidade de notas:")
if (notas50 > 0):
    print(notas50, "nota(s) de 50")
if (notas20 > 0):
    print(notas20, "nota(s) de 20")
if (notas10 > 0):
    print(notas10, "nota(s) de 10")
if (notas5 > 0):
    print(notas5, "nota(s) de 5")
if (notas1 > 0):
    print(notas1, "nota(s) de 1")
