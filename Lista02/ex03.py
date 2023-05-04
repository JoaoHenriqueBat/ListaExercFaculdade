"""
Como fazer para contar a quantidade de numeros pares entre dois numeros quaisquer
"""

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
numeros = [n1,n2]
menor = min(numeros)
maior = max(numeros)
contador_par = 0
while(menor < maior):
    menor+= 1
    if menor%2 == 0:
        contador_par+= 1

print(f"Quantidade de números pares é: {contador_par}")
        

