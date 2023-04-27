'''Escrever um algoritmo que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, informar o seu nome, o salário fixo e salário no final do mês.
'''

nome = input('Digite o nome do vendedor: ')
salario = float(input('Digite seu salário fixo mensal: '))
vendas = int(input('Digite a quantidade de vendas efetuadas no mês: '))

comissao = vendas * 0.15
salario_final = salario + comissao

print(f'{nome}')
print(f'Seu salário fixo é: R${salario}')
print(f'Seu salário final é de R$ {salario_final}')

