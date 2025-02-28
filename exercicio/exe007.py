#exe007
print("============= DESAFIO =============")
print("""7. Elabore um programa que receba dois números e pergunte ao usuário qual 
operação deseja realizar (soma, subtração, multiplicação ou divisão). Utilize estruturas
condicionais (if, elif, else) para efetuar a operação escolhida e exibir o resultado.""")
print("===================================")

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

print("O que deseja fazer?")

print("""[1] - Somar
[2] - Subtrair
[3] - Multiplicar
[4] - Dividir
""")

opcao = input("")
if opcao == "1":
    resultado = (n1+n2)
    print(f"A soma entre os dois é {resultado}")
elif opcao == "2":
    resultado = (n1 - n2)
    print(f"A subtração entre os dois é {resultado}")
elif opcao == "3":
    resultado = (n1 * n2)
    print(f"A multiplicação entre os dois é {resultado}")
elif opcao == "4":
    resultado = (n1 / n2)
    print(f"A divisão entre os dois é {resultado}")
else:
    print("Essa pção não existe!")


