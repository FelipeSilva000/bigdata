#exe020
print("============= DESAFIO =============")
print("""20. Crie uma lista vazia e peça para o usuário inserir 5 elementos nela (usando 
input dentro de um loop). Ao final, use o método .remove() para remover o último 
valor inserido e exiba a lista resultante.""")
print("===================================")


lista = []

for i in range(5):
    elemento = input(f"Digite um número: ")
    lista.append(elemento)
lista.remove(lista[-1])
print(f"Lista após a remoção do último elemento: {lista}")