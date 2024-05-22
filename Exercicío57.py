# Curso básico de Python
# Nome do Desenvolvedor: Gregory Klaus da Silva Pereira
# Versão: 1.0
# Exercício de Lógica de programação
# Com a linguagem de programação de Python
# Ler quatro valores referentes a quatro notas escolares de um aluno e imprimir uma mensagem dizendo se o aluno foi aprovado.


nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))
media = (nota1 + nota2 + nota3 + nota4) / 4
if media >= 5:
    print("O aluno foi aprovado com média", media)
else:
    print("O aluno foi reprovado com média", media)
print("Obrigado por utilizar nosso programa!")
