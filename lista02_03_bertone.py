'''
Nome: Bertone Porto
Data: 18/11/2024

3. Crie um programa que leia uma quantidade
não determinada de números inteiros. O
programa deve calcular e escrever a
quantidade de números pares e ímpares e a média
aritmética dos números pares.
A leitura deve ser encerrada quando
for lido o número
zero, que não deve ser considerado.

'''

qtd_pares = 0
qtd_impares = 0
soma_pares = 0

#leitura e processamento
numero = int(input('Digite número inteiro(0 para encerrar): '))

while (numero != 0):  #continua enquanto o número não for zero
    if (numero % 2 == 0):  #verifica se é par
        qtd_pares += 1
        soma_pares += numero
    else:  #caso contrário, é ímpar
        qtd_impares += 1
        
    numero = int(input('Digite número inteiro(0 para encerrar): '))

#calculo da média aritmética dos números pares
if qtd_pares > 0:
    media_pares = soma_pares / qtd_pares
else:
    media_pares = 0  #evita divisão por zero

#saída dos resultados
print("Quantidade de números pares:", qtd_pares)
print("Quantidade de números ímpares:", qtd_impares)
print("Média dos números pares:", media_pares)
