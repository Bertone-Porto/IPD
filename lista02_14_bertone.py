'''
Nome: Bertone Porto
Data: 19/11/24

14. Num frigorífico existem 90 bois.
Cada boi traz preso em seu pescoço um cartão
contendo seu número de identificação
e seu peso. Crie um programa que
escreva o número e peso do
boi mais gordo e do boi mais magro.
Além disso, responda: se houver
dois ou mais bois com o mesmo peso,
maior que todos os demais, este algoritmo
escreverá o número de qual deles?
'''
numero_mais_gordo = 0
peso_mais_gordo = 0

numero_mais_magro = 0
peso_mais_magro = 99999 

for i in range(1, 6):
    numero = int(input("Número do boi: "))
    peso = float(input("Peso do boi: "))
    
    #verifica se é o mais gordo
    if (peso > peso_mais_gordo):
        peso_mais_gordo = peso
        numero_mais_gordo = numero
    
    #verifica se é o mais magro
    if (peso < peso_mais_magro):
        peso_mais_magro = peso
        numero_mais_magro = numero

#resultados
print("Boi mais gordo: Número", numero_mais_gordo, "com peso", peso_mais_gordo, "kg")
print("Boi mais magro: Número", numero_mais_magro, "com peso", peso_mais_magro, "kg")
