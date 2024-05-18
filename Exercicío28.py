#Curso basico de Python
#Nome do Densenvolvedor:Gregory Klaus da Silva Pereira
#Versão: 1.0
#Exercicio de Lógica de programação
#Com a linguagem de programaçãõ de python
# Ler as notas da 1a. e 2a. avaliações de um aluno
# Calcular a média aritmética simples e escrever uma mensagem que diga se o aluno foi ou não aprovado (considerar que nota igual ou maior que 6 o aluno é aprovado). Escrever também a média calculada

print("Calcule sua nota aqui!!")
nota1=int(input("Digite a nota da primeira prova: "))
nota2=float(input("Digite a nota da segunda prova: "))
media=(nota1+nota2)/2
if media>6:
    print("Parábens!.Voce foi aprovado")
elif media<6:
    print("Que pena, Voce foi reprovado.Precisa se esforçar mais")
else:
    print("Voce passou, mas foi na risca.Estude um pouco mais.")
print("Obrigado")
