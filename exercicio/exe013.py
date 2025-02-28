#exe013
print("============= DESAFIO =============")
print("""13. Faça um programa que possua uma lista de 5 nomes quaisquer. Peça ao 
usuário um nome e informe em qual índice esse nome se encontra na lista. Caso 
não exista, mostre a mensagem “Nome não encontrado”""")
print("===================================")




lista = ["ana","paula","maria","lucas","joao"]

nome = str(input("Digite um nome : "))

if nome in lista:

    print(f"O nome {nome} está na lista na posição {lista.index(nome)}")
else:
    print(f"O nome não está na lista")