#Curso basico de Python
#Nome do Densenvolvedor:Gregory Klaus da Silva Pereira
#Versão: 1.0
#Exercicio de Lógica de programação
#Com a linguagem de programaçãõ de python
#As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas, calcule e escreva o custo total da compra.

print("Caculo do Valor")
maca=int(input("Digite a quantidade de maçãs: "))
if maca<12:
    custo=maca*1.30
else:
    custo=maca*1.0
custo=round(custo, 2)
print(f"O valor total das maçãs sao de R$:{custo}")
print("Obrigado. Volte Sempre")