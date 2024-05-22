#Curso basico de Python
#Nome do Densenvolvedor:Gregory Klaus da Silva Pereira
#Versão: 1.0
#Exercicio de Lógica de programação
#Com a linguagem de programaçãõ de python
#O custo de um carro novo ao consumidor é a soma do custo de fábrica com a porcentagem do 
#distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que o percentual do distribuidor 
#seja de 28% e os impostos de 45%, escrever um algoritmo para ler o custo de fábrica de um carro, 
#calcular e escrever o custo final ao consumidor.

print("Vamos comprar um carro")
custo_fabrica=float(input("Digite o valor de custo do carro para a fabrica: "))
porcentual_fabrica= 28/100
imposto= 45/100
valor_distribuicao=custo_fabrica*porcentual_fabrica
valor_imposto=custo_fabrica*imposto
valor_final=custo_fabrica+valor_distribuicao+valor_imposto
print(f"O valor do carro é de R$:{valor_final:.2f}")
print("Obrigado")