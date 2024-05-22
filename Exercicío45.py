# Curso básico de Python
# Nome do Desenvolvedor: Gregory Klaus da Silva Pereira
# Versão: 1.0
# Exercício de Lógica de programação
# Com a linguagem de programação de Python
# Tendo como dados de entrada o nome, a altura e o sexo (M ou F) de uma pessoa, calcule 
# e mostre seu peso ideal, utilizando as seguintes fórmulas: 
# - para sexo masculino: peso ideal = (72.7 * altura) - 58 
# - para sexo feminino: peso ideal = (62.1 * altura) - 44.7
nome = input("Digite o nome da pessoa: ")
altura = float(input("Digite a altura da pessoa (em metros): "))
sexo = input("Digite o sexo da pessoa (M ou F): ")

if sexo == 'M':
    peso_ideal = (72.7 * altura) - 58
elif sexo == 'F':
    peso_ideal = (62.1 * altura) - 44.7
else:
    print("Sexo inválido. Digite M para masculino ou F para feminino.")
    peso_ideal = None

if peso_ideal is not None:
    print("O peso ideal de", nome, "é:", peso_ideal, "kg")
