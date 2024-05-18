#Curso basico de Python
#Nome do Densenvolvedor:Gregory Klaus da Silva Pereira
#Versão: 1.0
#Exercicio de Lógica de programação
#Com a linguagem de programaçãõ de python
#Escreva um programa que peça ao usuário para digitar uma frase e conte quantas vogais (a, e, i, o, u) ela possui.

print("Vogais")
frase=input("Digite uma frase, para ver quantas vogais tem: ")
vogais="aeiouAEIOU"
contador=0
for char in frase:
    if char in vogais:
        contador+=1
print(f"A frase digitada tem {contador} vogais")
print("Obrigado por usar o programa!")
print("Volte Sempre")