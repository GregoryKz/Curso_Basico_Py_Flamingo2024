# Curso básico de Python
# Nome do Desenvolvedor: Gregory Klaus da Silva Pereira
# Versão: 1.0
# Exercício de Lógica de programação
# Com a linguagem de programação de Python
# Ler 3 valores (A, B e C) representando as medidas dos lados de um triângulo e escrever se formam 
# ou não um triângulo. OBS: para formar um triângulo, o valor de cada lado deve ser menor que a soma 
# dos outros 2 lados.


A = float(input("Digite o valor do lado A: "))
B = float(input("Digite o valor do lado B: "))
C = float(input("Digite o valor do lado C: "))
if (A < B + C) and (B < A + C) and (C < A + B):
    mensagem = "Os valores formam um triângulo."
else:
    mensagem = "Os valores NÃO formam um triângulo."
print(mensagem)
print("Obrigado por utilizar nosso programa!")