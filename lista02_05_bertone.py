'''
Nome: Bertone Porto
Data: 18/11/24

5. Crie um programa que leia a descrição,
o preço unitário e a quantidade de 10 produtos
comprados por uma empresa. Ao final deve
ser escrito o total gasto pela empresa e a
descrição do produto mais caro.
'''

total_gasto = 0
nome_mais_caro = ""
preco_mais_caro = 0

#leitura dos dados dos 10 produtos
for i in range(1, 5):
    print("Produto", i)
    descricao = input("Descrição: ")
    preco_unitario = float(input("Preço unitário: "))
    quantidade = int(input("Quantidade: "))
    
    #atualiza o total gasto
    total_gasto +=(preco_unitario * quantidade)
    
    #vrifica se é o produto mais caro
    if (preco_unitario > preco_mais_caro):
        preco_mais_caro = preco_unitario
        nome_mais_caro = descricao
    print('')
#saída dos resultados
print("Total gasto pela empresa: ", total_gasto)
print("Produto mais caro: ", nome_mais_caro)
