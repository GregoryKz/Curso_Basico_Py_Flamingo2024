#Curso basico de Python
#Nome do Densenvolvedor:Gregory Klaus da Silva Pereira
#Versão: 1.0
#Exercicio de Lógica de programação
#Com a linguagem de programaçãõ de python
#Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e escreva a idade 
#dessa pessoa expressa apenas em dias. Considerar ano com 365 dias e mês com 30 dias. 


print("Vamos calcular a sua idade em dias ?")
print("V amos considerar que o ano tem 365 dias, e o mês tem 30")
anos=int(input("Digite quantos anos vc tem: "))
meses=int(input("Digite quantos mêses, apos seu aniversario: "))
dias=int(input("Digite quantos dias apos o mês digitado"))
anos_em_dias=(anos*365)+(meses*30)+dias
print(f"Sua idade em dias são de {anos_em_dias} dias")
print("Obrigado")
