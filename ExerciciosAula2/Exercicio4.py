# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

import array as vetor

caracter = vetor.array("u", [])
counter = 0

while counter < 10:
    try:
        x = input("Digite um caracter: ")
        if (x != "a") and (x != "e") and (x != "i") and (x != "o") and (x != "u"):
            caracter.append(x)
        counter += 1
    except:
        print("Caracter inválido, digite novamente")

total = len(caracter)
print("Foram lidas", total, "consoantes.")

print("Consoantes:")
for x in caracter:
    print(x, end=", ")
