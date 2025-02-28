#exe012
print("============= DESAFIO =============")
print("""12. Dada a lista [10, 20, 30, 40, 50], escreva um programa que peça ao usuário um 
número e verifique se esse número está na lista. 
 - Exiba “Número encontrado” ou “Número não encontrado”.""")
print("===================================")

lista = [10,20,30,40,50]

num = int(input("Digite um número:  "))

if num in lista:
    print(f"O número {num} está na lista")
else:
    print(f"O número {num} não está na lista")