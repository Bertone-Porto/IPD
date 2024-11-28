'''
Nome: Bertone Porto
Data: 21/11/24

18. Crie um programa que leia
um número N e imprima os N
primeiros números primos.
'''
N = int(input("Digite a quantidade de números primos a exibir: "))

#geração dos N primeiros números primos
contador = 0  
numero = 2  

while (contador < N):
    primo = True
    for i in range(2, numero):
        if (numero % i == 0):
            primo = False  #marca como não primo
    if (primo):  #se for primo, exibe e incrementa o contador
        print(numero)
        contador += 1
    numero += 1  #próximo número a ser verificado
