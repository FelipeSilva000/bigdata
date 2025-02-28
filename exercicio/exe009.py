#exe009
print("============= DESAFIO =============")
print("""9. Escreva um programa que simule a tela de login de um sistema. 
 - Defina um usuário e senha fixos (por exemplo, usuario = "admin", senha = 
"1234").
 - Peça para o usuário digitar o usuário e a senha.
 - Caso estejam corretos, exiba “Login bem-sucedido!”; caso contrário, exiba 
“Usuário ou senha incorretos!”.""")
print("===========================================================")
print("")


usuario = "admin"
senha = "1234"

print("=========================")
print("==========LOGIN==========")
print("=========================")
print("Digite seu Usuario e senha")
chave1 = str(input("Usuario:"))
chave2 = str(input("Senha:"))

if (chave1==usuario) and (chave2==senha):
    print("Login bem-sucedido!")
    print(f"Bem vindo {usuario}")
else:
    print("Usuario ou senha incorretos")