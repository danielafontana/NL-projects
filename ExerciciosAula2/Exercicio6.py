# 6. Faça um Programa que imprima a data de hoje e quantos dias faltam para o final do ano.

from datetime import date, datetime

data_atual = date.today()
fim_de_ano = date(2021, 12, 31)

data_final = fim_de_ano - data_atual
date_format = "{}/{}/{}".format(data_atual.day, data_atual.month, data_atual.year)

print("Data atual:", date_format)
print("Faltam", data_final.days, "dias para o final do ano")
