'''
Nome: Bertone Porto
Data: 19/11/24

13. Crie um programa que:
a) Leia a idade de várias pessoas.
O final da lista contém o valor da idade igual a
-1 que não deverá ser computado.
b) Calcule e mostre a idade média
desse grupo de indivíduos. Escreva também a
porcentagem de pessoas entre 21 e 65 anos inclusive.

'''
soma_idades = 0
contador = 0
dentro_faixa = 0

idade = int(input("Digite as idades (-1 para encerrar): "))
while (idade != -1):
    if (idade > 0):  
        soma_idades += idade
        contador += 1
        if (21 <= idade <= 65):
            dentro_faixa += 1
    idade = int(input("Idade: "))

if (contador > 0):
    media = soma_idades/contador
    porcentagem_faixa = (dentro_faixa/contador)*100
    print("Idade média do grupo:", media)
    print("Porcentagem de pessoas entre 21 e 65 anos:", porcentagem_faixa, "%")
else:
    print("Nenhuma idade válida foi informada.")
