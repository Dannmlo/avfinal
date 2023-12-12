#Questao06- Positivos e Média:

print("Descubra quantos valores positivos e a média desses valores.")
#Criar lista "numeros" e variável "positivo".
numeros = []
positivo=0

#Repete uma ação 6 vezes
for i in range(0,6):
#Requer um valor para ser armazenado em na variável "numero"
    numero = float(input(f'Digite o {i+1}° número: '))
#Caso o número seja maior que 0 adicionar 1 na variável positivo, e adicionar-lo na lista "numeros".
    if numero>0:
        positivo = positivo+1
        numeros.append(numero)
#Soma todos os números positivos da lista "numeros".
soma = sum(numeros)

#Mostra a quantidade de valores positivos.
print(f"{positivo} valores positivos")

#Mostra a média dos valores positivos
print(f"{soma/positivo}")