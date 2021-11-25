# 7. Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

import array as vetor

numbers = vetor.array("i", [])
soma = 0
multi = 1

while len(numbers) < 5:
    try:
        numbers.append(int(input("Escreva um número: ")))
    except:
        print("Número inválido, digite novamente")

print("Números:")
for x in range(len(numbers)):
    print(numbers[x], end=", ")

for x in numbers:
    soma = soma + x
print("\nSoma:", soma)

for x in numbers:
    multi = multi * x
print("Multiplicação:", multi)
