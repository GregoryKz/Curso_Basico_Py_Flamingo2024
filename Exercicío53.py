# Curso básico de Python
# Nome do Desenvolvedor: Gregory Klaus da Silva Pereira
# Versão: 1.0
# Exercício de Lógica de programação
# Com a linguagem de programação de Python
# Uma posto está vendendo combustíveis com a seguinte tabela de descontos:
# - até 20 litros, desconto de 3% por litro Álcool 
# - acima de 20 litros, desconto de 5% por litro Álcool 
# - até 20 litros, desconto de 4% por litro Gasolina 
# - acima de 20 litros, desconto de 6% por litro Gasolina 
# Escreva um algoritmo que leia o número de litros vendidos e o tipo de combustível (codificado da 
# seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se 
# que o preço do litro da gasolina é R$ 3,30 e o preço do litro do álcool é R$ 2,90.

tipo_combustivel = input("Digite o tipo de combustível (A para Álcool, G para Gasolina): ")
litros = float(input("Digite o número de litros vendidos: "))
preco_gasolina = 3.30
preco_alcool = 2.90
if tipo_combustivel.upper() == 'A':
    if litros <= 20:
        valor_pagar = litros * (preco_alcool - (preco_alcool * 0.03))
    else:
        valor_pagar = litros * (preco_alcool - (preco_alcool * 0.05))
elif tipo_combustivel.upper() == 'G':
    if litros <= 20:
        valor_pagar = litros * (preco_gasolina - (preco_gasolina * 0.04))
    else:
        valor_pagar = litros * (preco_gasolina - (preco_gasolina * 0.06))
else:
    valor_pagar = 0
    print("Tipo de combustível inválido. Por favor, digite A para Álcool ou G para Gasolina.")
if valor_pagar > 0:
    print("O valor a ser pago pelo cliente é R$", round(valor_pagar, 2))
print("Obrigado por utilizar nosso programa!")