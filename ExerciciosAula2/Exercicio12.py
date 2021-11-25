# Nome ao contrário em maiúsculas. Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o
# nome do usuário de trás para frente utilizando somente letras maiúsculas.

nome = input("Informe o seu nome: ")

nome = nome.upper()

print(nome[::-1])
