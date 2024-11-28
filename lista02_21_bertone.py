'''
Nome: Bertone Porto
Data: 21/11/24

21. Crie um programa que leia um número N e calcule:

'''

N = int(input("Digite o valor de N: "))

#cálculo da soma
soma = 0
for i in range(1, N + 1):
    soma += 1 / i

#resultado
print("O valor da soma é:", soma)
