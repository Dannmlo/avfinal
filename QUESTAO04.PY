#Questao04- DDD:

#Tabela de DDD:
#61 = Brasilia
#71 = Salvador
#11 = São Paulo
#21 = Rio de Janeiro
#32 = Juiz de Fora
#19 = Campinas
#27 = Vitoria
#31 = Belo Horizonte


print("Descubra de onde é seu DDD\n")
#Iniciar o programa.

numero = int(input(f"Digite seu número de DDD (Brasileiro) \nObs: Não utilize espaços e nem sinais: "))
#Pedir o que o usuário insira o número de DDD

#Armazenar os numeros de DDD para comparar
if numero == 61:
    print("Brasília")
elif numero == 71:
    print("Salvador")
elif numero == 11:
    print("São Paulo")
elif numero == 21:
    print("Rio de Janeiro")
elif numero == 32:
    print("Juiz de Fora")
elif numero == 19:
    print("Campinas")
elif numero == 27:
    print("Vitória")
elif numero == 31:
    print("Belo Horizonte")
else:
    print("DDD não cadastrado")
#Caso o DDD não esteja cadastrado informar; DDD não cadastrado