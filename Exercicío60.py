# Curso básico de Python
# Nome do Desenvolvedor: Gregory Klaus da Silva Pereira
# Versão: 1.0
# Exercício de Lógica de programação
# Com a linguagem de programação de Python
# Apresentar o total da soma obtida dos cem primeiros números inteiros (1+2+3+4+...+98+99+100).

soma = 0
for i in range(1, 101):
    soma += i
print("O total da soma dos cem primeiros números inteiros é:", soma)
print("Obrigado por utilizar nosso programa!")