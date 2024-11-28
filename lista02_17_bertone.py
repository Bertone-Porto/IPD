'''
Nome: Bertone Porto
Data: 21/11/24

17. Crie um programa que leia um
número N e verifique se ele é primo.
'''

N = int(input("Digite um número: "))

if (N < 2):
    print(N, "não é primo.")
else:
    primo = True
    for i in range(2, N):
        if (N % i == 0):
            primo = False  #marca como não primo
    if (primo):
        print(N, "é primo.")
    else:
        print(N, "não é primo.")



