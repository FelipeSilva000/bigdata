#exe010
print("============= DESAFIO =============")
print("""10. Elabore um programa que calcule o fatorial de um número inteiro informado 
pelo usuário. 
 - Dica: use loop (for ou while) para efetuar o cálculo""")
print("===================================")


num = int(input("Digite um número: "))
fatorial = 1
resultado = ""

for i in range(num, 0, -1):  # Loop de num até 1 (decrescente)
    fatorial *= i
    if i == num:
        resultado += str(i)  # Primeiro número sem '*'
    else:
        resultado += f" * {i}"
print(f"{resultado} = {fatorial}")