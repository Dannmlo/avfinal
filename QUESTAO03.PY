#Questao03- Senha Fixa:
print("senha")
senha = 2002
#Guarda a senha.

tentativa = int(input("Digite a senha: "))
#Pedir senha ao usuário.

while tentativa != senha:
    print("Senha Invalida")
    tentativa = int(input("Digite a senha: "))
#Verificar as tentativas de senha do usuário, caso for a senha errada pedir a senha novamente em loop.

print("Acesso permitido")
#Caso o usuário digite a senha correta finalizar o código.