#exe019
print("============= DESAFIO =============")
print("""19. Faça um programa que leia um número inteiro N e crie uma lista contendo 
todos os números de 0 até N (inclusive). Depois, transforme essa lista em uma 
tupla e exiba o resultado.""")
print("===================================")

N = int(input("Digite um número inteiro: "))

lista_numeros = list(range(N + 1))

tupla_numeros = tuple(lista_numeros)


print(f"Lista: {lista_numeros}")
print(f"Tupla: {tupla_numeros}")