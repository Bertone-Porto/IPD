'''
Nome: Bertone Porto
Data: 19/11/24

10. Crie um programa que calcule
a soma dos primeiros 20 números
pares.
Os primeiros
números pares são: 2, 4, 6, ...
'''
soma = 0
contador = 0
numero = 2

while (contador < 20):
    soma += numero
    numero += 2
    contador += 1
print("A soma dos primeiros 20 números pares é: ", soma)
