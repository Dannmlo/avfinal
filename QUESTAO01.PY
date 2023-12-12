#Questao01- Imposto de Renda:

#Tabela de Imposto:
#R$0.00 - R$2000.00 = Isento
#R$2000.01 - R$3000.00= 8%
#R$3000.01 - R$4500.00 = 18%
#Acima de R$4500.00 = 28%


print("Verifique o quanto de impostos você precisa pagar")
salario = float(input("Digite seu salário: "))
#receber o salário do usuario para calcular o imposto

while salario < 0:
    print("\nDigite um salário válido.")
    salario = float(input("Digite seu salário: "))
#Verificar se o valor do salario e maior que R$0.00 para ser validado.

if salario <= 2000.00:
    print('Insento')
#Verificar se o valor está entre R$0.00 e R$2000.00, nao aplicar imposto.

elif salario > 2000.00 and salario < 3000.01: 
    print(f"R$ {salario*(8/100):.2f}")
#Verificar se o valor está entre R$2000.00 e R$3000.00, aplicar imposto de 8%.

elif salario > 3000.00 and salario < 4500.01:
    print(f"R$ {salario*(18/100):.2f}")
#Verificar se o valor é está entre R$3000.00 e R$4500.00, aplicar imposto de 18%.

else:
    print(f"R$ {salario*(28/100):.2f}")
#Verificar se o valor é acima de R$4500.00, aplicar imposto de 28%.