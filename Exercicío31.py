#Curso basico de Python
#Nome do Densenvolvedor:Gregory Klaus da Silva Pereira
#Versão: 1.0
#Exercicio de Lógica de programação
#Com a linguagem de programaçãõ de python
#Escreva um algoritmo para ler o salário mensal atual de um funcionário e o percentual de reajuste. Calcular e escrever o valor do novo salário.

print("Calcule seu almento ;)")
salario=float(input("Digite aqui o valor do seu salario atual:  "))
porcentual=float(input("Digite o porcentual de reajuste: "))
aumento=salario*(porcentual/100)
novo_salario=salario+aumento

print(f"O salario atual é R$:{salario}")
print(f"O porcentual de aumento é {porcentual}%")
print(f"O valor do aumento e de R$:{aumento}")
print(f"O valor do salario cm aumenro e de R$:{novo_salario}")
print("Obrigado por usar o programa")
