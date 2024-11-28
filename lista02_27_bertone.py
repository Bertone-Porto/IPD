'''
Nome: Bertone Porto
Data: 26/11/2024

27. Crie um programa que leia um número
(com qualquer número de dígitos) em uma
base numérica de ordem < 10 e calcule
o número correspondente na base decimal.
O número da ordem da base
(e.g., 2 para binária, 3 para ternária, 8 para octal, etc.) deve
também ser informado pelo usuário.

'''

base = int(input("Digite a base numérica (menor que 10): "))
numero = int(input("Digite o número na base: "))

decimal = 0
potencia = 0

#processamento dos dígitos do número
while (numero > 0):
    digito = numero % 10  #obtém o último dígito
    decimal += digito * (base ** potencia)
    potencia += 1
    numero //= 10  #remove o último dígito

#resultado
print("O número na base decimal é:", decimal)
