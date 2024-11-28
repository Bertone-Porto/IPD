'''
Nome: Bertone Porto
Data: 19/11/24

15. Crie um programa que:
a) Leia e escreva o nome e a altura
das moças inscritas em um concurso de
beleza, até que seja digitada o nome ‘MARIA’,
que marca o final da lista, mas é
para ser computada no concurso.

b) Calcule e escreva as duas maiores
alturas e quantas moças as possuem.

'''

maior1 = 0
maior2 = 0
quant_maior1 = 0
quant_maior2 = 0
finalizou = False

while (not finalizou):
    nome = input("Nome: ").upper()
    altura = float(input("Altura: "))
    
    #verifica as duas maiores alturas
    if (altura > maior1):
        maior2 = maior1
        quant_maior2 = quant_maior1
        maior1 = altura
        quant_maior1 = 1
        
    elif (altura == maior1):
        quant_maior1 += 1
        
    elif (altura > maior2):
        maior2 = altura
        quant_maior2 = 1
        
    elif (altura == maior2):
        quant_maior2 += 1

    #verifica se é 'maria'
    if (nome == "MARIA"):
        finalizou = True

#saída
print("A maior altura é:", maior1, "m (quantidade:", quant_maior1)
print("A segunda maior altura é:", maior2, "m (quantidade:", quant_maior2)

