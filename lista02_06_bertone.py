'''
Nome: Bertone Porto
Data: 18/11/24
6. Crie um programa que leia 2
números inteiros positivos, A e B,
e que calcule a soma
de todos os números compreendidos
entre eles. Os valores A e B não devem ser
considerados no somatório. Caso A
seja maior do que B deve ser
enviada uma
mensagem para o usuário
informando que a soma não será realizada.
'''

#leitura dos números A e B
print("Digite dois números inteiros positivos:")
A = int(input("A: "))
B = int(input("B: "))

#verifica se A é maior que B
if (A >= B):
    print("A soma não será realizada, A deve ser menor que B.")
else:
    soma = 0
    for i in range(A + 1, B):  #soma apenas os números entre A e B
        soma += i
    print("A soma dos números entre A e B é: ", soma)
