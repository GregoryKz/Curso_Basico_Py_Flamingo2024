# Curso básico de Python
# Nome do Desenvolvedor: Gregory Klaus da Silva Pereira
# Versão: 1.0
# Exercício de Lógica de programação
# Com a linguagem de programação de Python
# Apresentar os resultados de uma tabuada de multiplicar (de 1 até 10) de um número qualquer.


numero = int(input("Digite um número para calcular a tabuada: "))
print("Tabuada de", numero, ":")
for i in range(1, 11):
    print(numero, "x", i, "=", numero * i)
print("Obrigado por utilizar nosso programa!")