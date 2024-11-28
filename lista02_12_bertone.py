'''
Nome: Bertone Porto
Data: 19/11/24

12. Crie um programa para calcular
a área de um triângulo qualquer,
considerando que
são fornecidos os comprimentos
dos seus lados. Esse programa
não pode permitir a
entrada de dados inválidos, ou seja,
medidas menores ou iguais a 0.

'''

print("Digite os comprimentos dos lados do triângulo:")
a = float(input("Lado a: "))
b = float(input("Lado b: "))
c = float(input("Lado c: "))

#verificando os dados
if ((a>0) and (b>0) and (c>0) and (a+b>c) and (a+c>b) and (b+c>a)):
    #Fórmula de Heron
    s = (a + b + c)/2
    area = (s*(s - a)*(s - b)*(s - c))**0.5
    print("Área do triângulo:", area)
else:
    print("Os valores fornecidos não formam um triângulo válido.")
