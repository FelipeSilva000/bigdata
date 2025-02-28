#exe006
print("============= DESAFIO =============")
print("""6. Crie um programa que pergunte ao usuário quantos valores ele deseja inserir."
Em seguida, use um loop para ler essa quantidade de números e, ao final, exiba a
média aritmética deles.""")
print("===================================")

num = int(input("Digite quantos valores voçê quer: "))
total = 0
cont = 0
for c in range(num):
    soma = (int(input("digite um número")))
    total = (soma+total)
    cont = cont+1
    media = (total/cont)

print(f"A media dos valores é igual a {media:.3f}")

