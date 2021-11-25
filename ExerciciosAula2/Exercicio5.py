# 5. Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
# Armazene os números pares no vetor PAR e os números IMPARES no vetor ímpar. Imprima os três vetores.

import array as vetor

numbers = vetor.array("i", [])
par = vetor.array("i", [])
impar = vetor.array("i", [])

while len(numbers) < 20:
    try:
        x = int(input("Digite um número inteiro: "))
        numbers.append(x)
        if x != 0:
            if (x % 2) == 0:
                par.append(x)
            else:
                impar.append(x)
    except:
        print("Número inválido, digite novamente")

print("Números:")
for x in range(len(numbers)):
    print(numbers[x], end=", ")
print("\nPar:")
for x in range(len(par)):
    print(par[x], end=", ")
print("\nÍmpar:")
for x in range(len(impar)):
    print(impar[x], end=", ")
