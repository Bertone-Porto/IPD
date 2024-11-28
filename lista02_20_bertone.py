'''
Nome: Bertone Porto
Data: 21/11/24

20. Crie um programa que imprima os
4 primeiros números perfeitos.
'''

contador = 0
numero = 1

print("Os 4 primeiros números perfeitos são: ")

while (contador < 4):
    soma_divisores = 0
    for i in range(1, numero):
        if (numero % i == 0):
            soma_divisores += i
    if (soma_divisores == numero):
        print(numero)
        contador += 1
    numero += 1
