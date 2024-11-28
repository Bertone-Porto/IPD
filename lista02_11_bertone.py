'''
Nome: Bertone Porto
Data: 19/11/24

11. Crie um programa que calcule a
soma dos N primeiros números inteiros ímpares e
positivos. O valor de N deve ser lido do usuário.
'''
N = int(input("Digite o valor de N (quantidade de ímpares a somar): "))

soma = 0
contador = 0
numero = 1

while (contador < N):
    soma += numero
    contador += 1
    numero += 2

print("A soma dos primeiros", N, "números ímpares positivos é:", soma)
