# 8. Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor.
# Imprima a idade e a altura na ordem inversa a ordem lida.

import array as vetor

pessoa = 0
altura = vetor.array("f", [5])
idade = vetor.array("i", [])

while pessoa < 5:
    try:
        x = int(input("Digite a sua idade: "))
        idade.append(x)
        y = float(input("Digite a sua altura: "))
        altura.append(y)
        pessoa += 1
    except:
        print("Número inválido, digite novamente")

idade.reverse()
altura.reverse()

print("Idades: ")
for x in range(len(idade)):
    print(idade[x], end=", ")

print("\nAlturas: ")
for y in range(len(altura)):
    print(altura[y], end=", ")
