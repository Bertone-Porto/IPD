'''
Nome: Bertone Porto
Data: 27/11/2024

31. Leia um número N inteiro.
Calcule sua raiz inteira.
Exemplo: N=21, raiz inteira = 4.
'''

N = int(input("Digite um número: "))

#cálculo da raiz inteira
raiz = 0
while (((raiz + 1) ** 2) <= N):
    raiz += 1

print("Raiz inteira: ", raiz)
