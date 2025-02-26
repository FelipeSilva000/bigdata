#exe005
print("============= DESAFIO =============")
print("5. Faça um programa que leia um número inteiro e verifique se ele é maior que 10."
      "Em caso afirmativo, exiba “Maior que 10”, caso contrário, “Não é maior que 10”.")
print("===================================")

num = int(input("digite um número: "))
if num > 10:
    print(f"{num} é maior que 10")
elif num == 10:
    print(f"{num} é igual a 10")
else:
    print(f"{num} é menor que 10")