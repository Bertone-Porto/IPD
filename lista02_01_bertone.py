'''
Nome: Bertone Porto
Data de criação: 18/11/2024

1. A prefeitura de uma cidade resolveu fazer uma
pesquisa entre os seus trabalhadores.
Para isso ela coletou alguns dados como idade,
sexo (M ou F) e salário. Crie um programa
que leia estes dados e que escreva ao final:
a) a média salarial dos homens, a média salarial das mulheres;
b) o maior salário encontrado entre as pessoas abaixo de 30 anos.
Obs.: O final da leitura de dados é marcado por uma idade negativa.
'''

#setando os valores bases
mediaM = 0
mediaF = 0
somaSalarioM = 0
somaSalarioF = 0
qtdM = 0
qtdF = 0
maiorSalario = -1

idade = 0
while(idade >= 0): #se idade for negativa, acaba o loop
    print(" ")

    #entrada dos valores
    idade = int(input('Idade: '))
    if(idade >=0):
        sexo = (input('Sexo (M ou F): ')).upper()
        salario = float(input('Salario: '))

        #se for sexo M, soma +1 na quantidade e soma o salário no total
        if(sexo == 'M'):
            qtdM += 1
            somaSalarioM += salario
            
        #se for sexo F, soma +1 na quantidade e soma o salário no total
        if(sexo == 'F'):
            qtdF += 1
            somaSalarioF += salario

        #verifica se o salario é maior que o atual em caso de ser maior ou igual a 30 anos
        if(salario >= maiorSalario and idade <= 30):
                maiorSalario = salario


#verificando para evitar divisão por zero
if(qtdM > 0):
    mediaM = (somaSalarioM)/qtdM
if(qtdF > 0):
    mediaF = (somaSalarioF)/qtdF


#saídas
print("------------------------------------")
print("a)")
print('Media salarial dos homens: ', mediaM)
print('Media salario das mulheres: ', mediaF)
print("------------------------------------")

print('')

print("------------------------------------")
print("b)")
print('Maior salario abaixo de 30 anos: ', maiorSalario)
print("------------------------------------")


