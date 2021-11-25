# 11. Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento.
# Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.


string1 = input("Informe a primeira palavra:")
string2 = input("Informe a segunda palavra:")

print("Palavra:", string1, "Comprimento:", len(string1))
print("Palavra:", string2, "Comprimento:", len(string2))

if len(string1) == len(string2):
    print("As palavras possuem o mesmo comprimento")
else:
    print("As palavras possuem comprimentos diferentes.")

if string1 == string2:
    print("As palavras são iguais no conteúdo")
else:
    print("As palavras são diferentes no conteúdo")
