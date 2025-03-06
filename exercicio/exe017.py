#exe017
print("============= DESAFIO =============")
print("""17. Elabore um programa que crie um dicionário cujas chaves sejam os números 
de 1 a 5 e os valores sejam o quadrado de cada chave. (Exemplo: {1:1, 2:4, 3:9, 
4:16, 5:25})""")
print("===================================")


quadrados = {num: num**2 for num in range(1, 6)}

print(quadrados)