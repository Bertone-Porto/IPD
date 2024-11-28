'''
Nome: Bertone Porto
Data: 27/11/2024

32. Elabore um programa que calcule
a quantidade de dias existentes entre duas datas.
Dica: utilize as variáveis
D1, M1, A1, D2, M2, A2. Por hipótese,
as variáveis dos anos não
precisam considerar a correção do
calendário gregoriano. Lembre-se que há regras
especiais de anos bissextos conforme o ano específico.
'''
#datas
print("Digite a primeira data (D M A):")
D1 = int(input("Dia: "))
M1 = int(input("Mês: "))
A1 = int(input("Ano: "))

print("Digite a segunda data (D M A):")
D2 = int(input("Dia: "))
M2 = int(input("Mês: "))
A2 = int(input("Ano: "))

#número de dias em cada mês(não bissexto)
dias_jan = 31
dias_fev = 28
dias_mar = 31
dias_abr = 30
dias_mai = 31
dias_jun = 30
dias_jul = 31
dias_ago = 31
dias_set = 30
dias_out = 31
dias_nov = 30
dias_dez = 31

#verifica se é ano bissexto se:
#regra 1: se o ano for divisível por 4, ele é um ano bissexto.
#regra 2: exceto se o ano for divisível por 100, mas não por 400.
if (((A1 % 4 == 0) and (A1 % 100 != 0)) or (A1 % 400 == 0)):
    dias_fev_ano1 = 29
else:
    dias_fev_ano1 = 28

if (((A2 % 4 == 0) and (A2 % 100 != 0)) or ((A2 % 400 == 0))):
    dias_fev_ano2 = 29
else:
    dias_fev_ano2 = 28

#cálculo dos dias totais para a primeira data (D1, M1, A1)
dias1 = D1
if (M1 > 1):
    dias1 += dias_jan
if (M1 > 2):
    dias1 += dias_fev_ano1
if (M1 > 3):
    dias1 += dias_mar
if (M1 > 4):
    dias1 += dias_abr
if (M1 > 5):
    dias1 += dias_mai
if (M1 > 6):
    dias1 += dias_jun
if (M1 > 7):
    dias1 += dias_jul
if (M1 > 8):
    dias1 += dias_ago
if (M1 > 9):
    dias1 += dias_set
if (M1 > 10):
    dias1 += dias_out
if (M1 > 11):
    dias1 += dias_nov

for ano in range(1, A1):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        dias1 += 366
    else:
        dias1 += 365

#cálculo dos dias totais para a segunda data (D2, M2, A2)
dias2 = D2
if (M2 > 1):
    dias2 += dias_jan
if (M2 > 2):
    dias2 += dias_fev_ano2
if (M2 > 3):
    dias2 += dias_mar
if (M2 > 4):
    dias2 += dias_abr
if (M2 > 5):
    dias2 += dias_mai
if (M2 > 6):
    dias2 += dias_jun
if (M2 > 7):
    dias2 += dias_jul
if (M2 > 8):
    dias2 += dias_ago
if (M2 > 9):
    dias2 += dias_set
if (M2 > 10):
    dias2 += dias_out
if (M2 > 11):
    dias2 += dias_nov

for ano in range(1, A2):
    if ( ((ano % 4 == 0) and (ano % 100 != 0)) or (ano % 400 == 0) ):
        dias2 += 366
    else:
        dias2 += 365

#diferença de dias
if (dias2 > dias1):
    diferenca = dias2 - dias1
else:
    diferenca = dias1 - dias2

#resultado
print("A quantidade de dias entre as duas datas é:", diferenca)
