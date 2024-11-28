'''
Nome: Bertone Porto
Data: 21/11/24

19. Crie um programa que leia um número N
e imprima se ele é perfeito ou não.
Um número é perfeito quando a
soma dos seus divisores é igual a
ele mesmo, e.g., 6 = 3 + 2 + 1.
'''
N = int(input("Digite um número: "))

soma_divisores = 0

for i in range(1, N):
    if (N % i == 0):
        soma_divisores += i

#verificação se é perfeito
if soma_divisores == N:
    print(N, "é um número perfeito.")
else:
    print(N, "não é um número perfeito.")
