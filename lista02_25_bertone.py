'''
Nome: Bertone Porto
Data: 25/11/24

25. Crie um programa que leia N números
inteiros positivos e responda se é possível
formar um polígono com o mesmo.
Dica: maior número < soma dos demais números.
'''

N = int(input("Digite a quantidade de números: "))

maior = 0  
soma = 0  

for i in range(N):
    numero = int(input("Digite o número: "))
    
    soma += numero  #adiciona o número à soma 

    #atualiza o maior número se o número atual for maior
    if (numero > maior):
        maior = numero  

#verificação 
if (maior < (soma - maior)):
    print("É possível formar um polígono.")
else:
    print("Não é possível formar um polígono.")
