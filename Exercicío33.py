#Curso basico de Python
#Nome do Densenvolvedor:Gregory Klaus da Silva Pereira
#Versão: 1.0
#Exercicio de Lógica de programação
#Com a linguagem de programaçãõ de python
# Faça um algoritmo que leia três notas de um aluno, calcule e escreva a média final deste aluno.
# Considerar que a média é ponderada e que o peso das notas é 2, 3 e 5.

print("Calcule sua nota")
nota1=int(input("Digite a primeira nota: "))
nota2=int(input("Digite a segunda nota: "))
nota3=int(input("Digite a terceira nota: "))
media_final =(nota1*2+nota2*3+nota3*5)/10
print(f"Sua media é de:{media_final}")
print("Obrigado")