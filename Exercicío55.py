# Curso básico de Python
# Nome do Desenvolvedor: Gregory Klaus da Silva Pereira
# Versão: 1.0
# Exercício de Lógica de programação
# Com a linguagem de programação de Python
# Elaborar um programa que apresente no final o somatório dos valores pares existentes na faixa de 1 até 500.

soma_pares = 0
for i in range(1, 501):
    if i % 2 == 0:
        soma_pares += i
print("O somatório dos valores pares de 1 até 500 é:", soma_pares)
print("Obrigado por utilizar nosso programa!")