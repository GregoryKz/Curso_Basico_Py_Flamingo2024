# Curso básico de Python
# Nome do Desenvolvedor: Gregory Klaus da Silva Pereira
# Versão: 1.0
# Exercício de Lógica de programação
# Com a linguagem de programação de Python
# Ler o salário fixo e o valor das vendas efetuadas pelo vendedor de uma empresa. Sabendo-se que 
# ele recebe uma comissão de 3% sobre o total das vendas até R$ 1.500,00 mais 5% sobre o que 
# ultrapassar este valor, calcular e escrever o seu salário total.

salario_fixo = float(input("Digite o salário fixo do vendedor: "))
valor_vendas = float(input("Digite o valor das vendas efetuadas pelo vendedor: "))

if valor_vendas <= 1500:
    comissao = valor_vendas * 0.03
else:
    comissao = (1500 * 0.03) + ((valor_vendas - 1500) * 0.05)
salario_total = salario_fixo + comissao
print("O salário total do vendedor é: R$", salario_total)
print("Obrigado por utilizar nosso programa!")