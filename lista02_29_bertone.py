'''
Nome: Bertone Porto
Data: 27/11/2024

29. Seu programa deve ler as variáveis
inteiras A e B. Posteriormente,
calcule o Máximo
Divisor Comum (MDC) entre A e B
e a quantidade de divisores comuns entre A e B.
'''
A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))

if (A > B):
    maior = A
else:
    maior = B
mdc = 1

for i in range(1, maior + 1):
    if ((A % i == 0) and (B % i == 0)):
        mdc = i

#contagem dos divisores comuns
quantidade_divisores_comuns = 0
for i in range(1, maior + 1):
    if ((A % i == 0) and (B % i == 0)):
        quantidade_divisores_comuns += 1

#resultados
print("MDC:", mdc)
print("Quantidade de divisores comuns:", quantidade_divisores_comuns)
