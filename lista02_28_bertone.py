'''
Nome: Bertone Porto
Data: 28/11/2024

28. Crie um programa que leia um
número decimal (com qualquer número de dígitos) e
o converta para a base hexadecimal.
'''
n10 = int(input("Entre com um número na base 10: "))
hexadecimal = ""

#o número decimal é dividido repetidamente por 16
#o resto da divisão determina o dígito da base hexadecimal
#dgitos entre 0 e 9 são mapeados para os caracteres '0' a '9' usando chr(48 + resto)
#dígitos entre 10 e 15 (hexadecimal A a F) são convertidos usando chr(55 + resto)
while (n10 > 0):
    resto = n10 % 16  #calcula o resto (dígito hexadecimal)
    if (resto < 10):
        hexadecimal = chr(48 + resto) + hexadecimal  #converte para '0-9' e adiciona no início
    else:
        hexadecimal = chr(55 + resto) + hexadecimal  #converte para 'A-F' e adiciona no início
    n10 //= 16

print("Número na base hexadecimal:", hexadecimal)
