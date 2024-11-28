'''
Nome: Bertone Porto
Data: 18/11/24

8. Crie um programa que apure os votos
de uma eleição municipal, numa cidade com
20.000 eleitores, onde concorreram
quatro candidatos. Um servidor da Justiça Eleitoral
digitará cada voto individualmente.
Cada voto equivale a um número inteiro. Os votos
válidos podem ser 1, 2, 3 e 4,
e estão relacionados aos seguintes candidatos:
1 – João da Silva; 2 – José Ramalho;
3 – Maria Mattos; e 4 – Pedro Américo.
Votos com o valor 0
devem ser contabilizados como votos
em branco, e votos com qualquer outro valor
(além de 0, 1, 2, 3 e 4), devem ser
considerados votos nulos. Calcule e
escreva o total de
votos de cada candidato, o
total de votos brancos e o total de votos nulos.
'''

#inicialização das variáveis
votos_joao = 0
votos_jose = 0
votos_maria = 0
votos_pedro = 0
votos_brancos = 0
votos_nulos = 0

print("Digite os votos. Use 0 para voto em branco: ")

for i in range(20000):
    voto = int(input("Voto do eleitor: "))
    if (voto == 1):
        votos_joao += 1
    elif (voto == 2):
        votos_jose += 1
    elif (voto == 3):
        votos_maria += 1
    elif (voto == 4):
        votos_pedro += 1
    elif (voto == 0):
        votos_brancos += 1
    else:
        votos_nulos += 1

#resultados
print('')
print("*********Resultado da eleição*********")
print("1 – João da Silva:", votos_joao, "votos")
print("2 – José Ramalho:", votos_jose, "votos")
print("3 – Maria Mattos:", votos_maria, "votos")
print("4 – Pedro Américo:", votos_pedro, "votos")
print("Votos brancos:", votos_brancos)
print("Votos nulos:", votos_nulos)
print('**************************************')
