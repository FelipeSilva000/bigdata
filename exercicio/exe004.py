#exe004
print("============= DESAFIO =============")
print("4. Escreva um programa que peça um valor em graus Fahrenheit (F) e converta para graus Celsius (C).")
print("   FORMULA : C = 5 * (F - 32) / 9")
print("===================================")

F = float(input("Digite a temperatura Fahrenheit: "))
C = ( 5 * (F-32)/9 )
print(f"O valor em graus celsius é {C:.3f} ")