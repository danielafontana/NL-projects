# 9. Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos dos elementos do vetor.

import array as vetor

vetor_A = vetor.array("i", [])
soma = 0

while len(vetor_A) < 10:
    try:
        vetor_A.append(int(input("Escreva um número inteiro: ")))
    except:
        print("Número inválido, digite novamente")

for x in vetor_A:
    print(x)
    soma += x

print("Soma:", soma)
