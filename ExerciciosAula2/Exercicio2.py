# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

import array as vetor

numbers = vetor.array("i", [])

while len(numbers) < 10:
    try:
        numbers.append(int(input("Escreva um número: ")))  # int ou float? =/
    except:
        print("Número inválido, digite novamente")

numbers.reverse()

print("Números na ordem inversa:")
for x in numbers:
    print(x, end=", ")
