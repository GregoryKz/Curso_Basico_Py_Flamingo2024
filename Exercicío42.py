#Curso basico de Python
#Nome do Densenvolvedor:Gregory Klaus da Silva Pereira
#Versão: 1.0
#Exercicio de Lógica de programação
#Com a linguagem de programaçãõ de python
#Uma revendedora de carros usados paga a seus funcionários vendedores um salário fixo por mês, 
#mais uma comissão também fixa para cada carro vendido e mais 5% do valor das vendas por ele 
#efetuadas. Escrever um algoritmo que leia o número de carros por ele vendidos, o valor total de suas 
#vendas, o salário fixo e o valor que ele recebe por carro vendido. Calcule e escreva o salário final do 
#vendedor. 

print("Calcule seu salario de acordo com suas vendas")
carros_vendidos = int(input("Digite a quantidade de carros vendidos: "))
valor_de_vendas = float(input("Digite o valor total de vendas: "))
salario_fixo = float(input("Digite seu salario fixo: "))
comissao_por_carro = float(input("Digite a valor da comissão por carro vendido: "))
comissao_total = carros_vendidos*comissao_por_carro
bonus_vendas = 0.5*comissao_por_carro
salario_final = salario_fixo+comissao_total+bonus_vendas
print(f"O seu salrio final e de R$:{salario_final:.2f}")
print("Obrigado por udar o programa")