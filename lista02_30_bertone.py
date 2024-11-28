'''
Nome: Bertone Porto
Data: 27/11/2024

30. Faça a fatoração de um numero
A inteiro, que é uma entrada do usuário.
Supondo,
por exemplo, que A seja igual a 12, sua saída de ser:
2 ^ 2
3 ^ 1
'''
A = int(input("Digite um número para fatoração: "))

fator = 2
while (A > 1):
    expoente = 0
    while (A % fator == 0):
        A //= fator
        expoente += 1
    if (expoente > 0):
        print(fator, "^", expoente)
    fator += 1
