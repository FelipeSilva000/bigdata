#exe008
print("============= DESAFIO =============")
print("""8. Faça um programa que leia uma palavra e verifique se ela é um palíndromo (ou 
seja, se lida de trás para frente permanece igual). Caso seja, exiba “É palíndromo”, 
caso contrário, “Não é palíndromo” """)
print("===================================")


palavra = str(input("Digite uma palavra : "))
palavra_min = palavra.lower()
palavra_inv = palavra_min[::-1]
if palavra_inv == palavra_min:
    print("Esta palavra é  um palíndromo")
else:
    print("Esta palavra não é um palíndromo")