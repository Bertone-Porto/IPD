'''
Nome: Bertone Porto
Data: 18/11/24

4. Crie um programa que leia os nomes
e os preços dos produtos de uma loja e que
escreva o nome do produto mais caro.
Considere que o final da lista é marcado pelo
produto ‘XXX’ e que não existem preços repetidos.
'''
nome_mais_caro = ""
preco_mais_caro = -1
nome = ''

while (nome != 'XXX'):
    #leitura do produto
    nome = input("Nome do produto(XXX para encerrar): ")
    if(nome != 'XXX'):
        preco = float(input("Preço do produto: "))
    
        #verifica se é o produto mais caro
        if (preco > preco_mais_caro):
            preco_mais_caro = preco
            nome_mais_caro = nome

#saída do resultado
print("Produto mais caro: ", nome_mais_caro)
