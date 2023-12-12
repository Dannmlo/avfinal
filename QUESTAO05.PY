#Questao05- Pares entre Cinco Números:

print("Contar valores de pares")
#Criar lista 'numeros' e 'par', e armazenar 
numeros = []
par=0

for i in range(0,5):
#Refazer a ação 5 vezes para verificar os pares

    numero = int(input(f'Digite o {i+1}° número: '))
#Pedir que o usuário insira os 5 números.

    if numero % 2 == 0:
        par = par+1
#Divisão para verificar quais números são pares.
#Caso o número for par adiciona-lo a variável "par".

print(f"{par} valores pares")
#Imprimir quantos números pares existem na lista.