'''
Nome: Bertone Porto
Data de criação: 18/11/2024

2. Crie um programa que escreva os N
primeiros termos de uma progressão aritmética
(PA). O primeiro termo e a
razão da PA devem ser informados pelo usuário.

'''
limite = 0

a1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
N = int(input('Digite o valor de N: '))
valor = a1

print(a1)
while(N != limite):
    print('')
    valor += r
    print(valor)

    limite += 1

