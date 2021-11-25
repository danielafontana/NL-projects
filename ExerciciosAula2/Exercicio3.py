# Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

import array as vetor

notas = vetor.array("f", [])
soma = 0

while len(notas) < 4:
    try:
        notas.append(float(input("Escreva um número: ")))
    except:
        print("Número inválido, digite novamente")

print("Notas:")

for x in notas:
    print(x)
    soma += x

print("Média:", (soma / 4))
