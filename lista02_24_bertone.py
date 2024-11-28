'''
Nome: Bertone Porto
Data: 25/11/24

24. Crie um programa que leia as taxas
de juros (r) de um financiamento price
(1% é igual a 0,01), os valores das parcelas
(pmt) e o número de parcelas (n).
Em seguida, calcule o
valor presente do financiamento que
é feito pela seguinte fórmula:
'''

r = float(input("Digite a taxa de juros (r): "))
pmt = float(input("Digite o valor das parcelas (pmt): "))
n = int(input("Digite o número de parcelas (n): "))

#cálculo do valor presente
vp = 0
for i in range(1, n + 1):
    vp += pmt / ((1 + r) ** i)

#resultado
print("O valor presente do financiamento é:", vp)
