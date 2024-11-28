'''
Nome: Bertone Porto
Data: 18/11/24

9. Uma empresa lançou um novo
produto no mercado e fez uma
pesquisa para saber se
os consumidores estavam satisfeitos,
para isso eles deveriam responder
sim ‘S’ ou não ‘N’.
Crie um programa que leia
a resposta de todas as pessoas e
escreva a porcentagem
dos que disseram sim e dos que
disseram não.
Obs.: O final da leitura de dados
é marcado pela resposta ‘F’.

'''
#inicialização das variáveiss
sim = 0
nao = 0
total_respostas = 0
resposta = ""

print("Digite as respostas da pesquisa ('S' para sim, 'N' para não, 'F' para finalizar):")

#leitura das respostas
while (resposta != "F"):
    resposta = input("Resposta: ").upper()
    if (resposta == "S"):
        sim += 1
        total_respostas += 1
    elif (resposta == "N"):
        nao += 1
        total_respostas += 1

#porcentagens
if (total_respostas > 0):
    porcentagem_sim = (sim/total_respostas) * 100
    porcentagem_nao = (nao/total_respostas) * 100
else:
    porcentagem_sim = 0
    porcentagem_nao = 0

#resultados
print("Porcentagem de respostas 'Sim':", porcentagem_sim, "%")
print("Porcentagem de respostas 'Não':", porcentagem_nao, "%")
