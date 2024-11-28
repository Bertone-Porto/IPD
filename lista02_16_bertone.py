'''
Nome: Bertone Porto
Data: 19/11/24

16. Certa firma fez uma pesquisa para
saber se as pessoas gostaram ou não de
um novo
produto lançado no mercado.
Para isso, forneceu o sexo do
entrevistado e sua resposta
(sim ou não). Sabendo-se que
foram entrevistadas 20 pessoas,
crie um algoritmo que
calcule e escreva:
a) o número de pessoas que responderam sim;
b) o número de pessoas que responderam não;
c) a porcentagem de pessoas do sexo masculino que responderam não.
'''

sim_total = 0
nao_total = 0
nao_masculino = 0
masculino_total = 0

for i in range(20):
    sexo = input("Sexo do entrevistado (M/F): ").upper()
    resposta = input("Resposta ao produto (S/N): ").upper()
    
    if (resposta == "S"):
        sim_total += 1
    elif (resposta == "N"):
        nao_total += + 1
        if (sexo == "M"):
            nao_masculino += 1
    if (sexo == "M"):
        masculino_total += + 1

#porcentagem
if (masculino_total > 0):
    porcentagem_nao_masculino = (nao_masculino/masculino_total)*100
else:
    porcentagem_nao_masculino = 0

#saída
print("Número de pessoas que responderam SIM:", sim_total)
print("Número de pessoas que responderam NÃO:", nao_total)
print("Porcentagem de homens que responderam NÃO:", porcentagem_nao_masculino, "%")
