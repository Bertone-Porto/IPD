'''
Nome: Bertone Porto
Data: 18/11/24

7. Crie um programa que leia 2 números
inteiros positivos, A e B, e que calcule a soma
de todos os números múltiplos de 4
compreendidos entre eles. Os valores A e B não
devem ser considerados no somatório.
Caso A seja maior do que B deve ser enviada uma
mensagem para o usuário informando
que a soma não será realizada.
'''

#leitura 
print("Digite dois números inteiros positivos: ")
A = int(input("A: "))
B = int(input("B: "))

# Verifica se A é maior que B
if (A >= B):
    print("A soma não será realizada, pois A deve ser menor que B")
else:
    soma = 0
    for numero in range(A+1, B):  #soma apenas os números entre A e B
        if numero % 4 == 0:  #verifica se é múltiplo de 4
            soma += numero
    print("A soma dos múltiplos de 4 entre A e B é: ", soma)
