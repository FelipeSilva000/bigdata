#exe015
print("============= DESAFIO =============")
print("""15. Dada a tupla (1, 2, 3, 4, 5), tente alterar o valor do índice 0 para 10. Observe o 
que ocorre e explique o motivo de qualquer erro.""")
print("===================================")



tupla = (1, 2, 3, 4, 5)

tupla[0] = 10
print(tupla)

#error: TypeError: 'tuple' object does not support item assignment
#tuplas são imutaveis