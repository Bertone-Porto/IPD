'''
Nome: Bertone Porto
Data: 26/11/2024

26. Crie um programa que verifique se existe alguma raiz na equação
Ax^3+ Bx^2+ Cx+D
no intervalor [-1.000, 1.000].
Seu algoritmo deve ler os coeficientes A, B, C e D.
Dica: incremente o valor de x
de uma unidade a cada interação e
verifique se houve uma
mudança de sinal no resultado da
equação, se o sinal mudou, existe
a ocorrência de uma
raiz (não é necessário calcular a raiz).
'''


# Nome: Bertone Porto
# Data: 26/11/2024

# Leitura dos coeficientes
A = float(input("Digite o coeficiente A: "))
B = float(input("Digite o coeficiente B: "))
C = float(input("Digite o coeficiente C: "))
D = float(input("Digite o coeficiente D: "))

x = -1000
raiz_existe = False

#continua enquanto não encontrar a raiz
while ((x < 1000) and (not raiz_existe)):  
    resultado_atual = (A * x**3) + (B * x**2) + (C * x + D)
    x_prox = x + 1
    resultado_prox = (A * x_prox**3) + (B * x_prox**2) + (C * x_prox + D)

    if ((resultado_atual * resultado_prox) < 0):
        raiz_existe = True  #atualiza a variável para indicar que uma raiz foi encontrada

    x += 1

#resultado
if (raiz_existe):
    print("Existe pelo menos uma raiz no intervalo [-1.000, 1.000].")
else:
    print("Não há raízes no intervalo [-1.000, 1.000].")
