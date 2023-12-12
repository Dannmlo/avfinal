#Questao02- Aumento de salário:
#
#Tabela de salários:
#0.00 - 400.00 = 15%
#400.01 - 800.00= 12%
#800.01 - 1200.00 = 10%
#1200.01 - 2000.00 = 7%
#Acima de 2000.00 = 4%

print("Descubre o valor do seu aumento.")
#receber o salário do usuario para calcular o novo salário.
salario = float(input("Digite o seu salário antigo: "))

while salario < 0:
    print('\nDigite um valor válido!')
    salario = float(input("Qual seu salário atual: "))
#Verificar se o valor do salario e maior que 0 para ser validado.

if salario <= 400:
    print(f'''
        Novo salário: {salario+(salario*(15/100)):.2f}
        Reajuste ganho: {salario*(15/100):.2f}
        Em percentual: 15 %
        ''')
#Verificar se o valor do salário é menor que R$ 400.00.


elif salario > 400 and salario <= 800:
    print(f'''
        Novo salário: {salario+(salario*(15/100)):.2f}
        Reajuste ganho: {salario*(15/100):.2f}
        Em percentual: 12 %
        ''')
#Verificar se o valor está entre 400R$ e 800R$, o aumento no salário sera de 12%

elif salario > 800 and salario <= 1200:
    print(f'''
        Novo salário: {salario+(salario*(15/100)):.2f}
        Reajuste ganho: {salario*(15/100):.2f}
        Em percentual: 10 %
        ''')
#Verificar se o valor está entre 800R$ e 1200R$, o aumento no salário sera de 10%.

elif salario > 1200 and salario <= 2000:
    print(f'''
        Novo salário: {salario+(salario*(15/100)):.2f}
        Reajuste ganho: {salario*(15/100):.2f}
        Em percentual: 7 %
        ''')
#Verificar se o valor está entre 1200R$ e 2000R$, o aumento no salário sera de 7%.

else:
    print(f'''
        Novo salário: {salario+(salario*(4/100)):.2f}
        Reajuste ganho: {salario*(4/100):.2f}
        Em percentual: 4 %
        ''')
#Verificar se o valor é maior do que 2000, o aumento no salário será de 4%.