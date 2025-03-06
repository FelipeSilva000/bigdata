#exe018
print("============= DESAFIO =============")
print("""18. Crie um dicionário que mapeie códigos de produtos (chave) para seus preços 
(valor). Em seguida, peça ao usuário para digitar um código e, caso exista, mostre 
o preço correspondente.""")
print("===================================")

produtos = {
    "cod001": 29.90,
    "cod002": 45.50,
    "cod003": 99.99,
    "cod004": 10.75,
    "cod005": 5.60
}

codigo = input("Digite o código do produto: ").strip().lower()

if codigo in produtos:
    print(f"O preço do produto {codigo} é R$ {produtos[codigo]:.2f}")
else:
    print("Código de produto não encontrado.")