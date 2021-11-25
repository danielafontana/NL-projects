# Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
import array as vetor

numbers = vetor.array("i", [])

while len(numbers) < 5:
    try:
        numbers.append(int(input("Escreva um número inteiro: ")))
    except:
        print("Número inválido, digite novamente")

for x in numbers:
    print(x, end=", ")
