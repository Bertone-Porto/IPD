'''
Nome: Bertone Porto
Data: 23/11/24

23. Crie um programa se imprima os N
primeiros números que sejam primos e façam
parte da série de Fibonacci.

'''

N = int(input("Digite o valor de N: "))

#variáveis para a sequência de Fibonacci
a = 0
b = 1
contador = 0

print("Os", N, "primeiros números que são primos e fazem parte da série de Fibonacci:")

while contador < N:
    #verificar se o número atual de Fibonacci é primo
    if (a > 1): 
        primo = True
        for i in range(2, int(a ** 0.5) + 1):  #testa divisores de 2 até sqrt(a)
            if (a % i == 0):
                primo = False
        if (primo):  #imprime e incrementa o contador se for primo
            print(a)
            contador += 1
    
    #avançar na sequência de Fibonacci
    temp = a + b
    a = b
    b = temp
