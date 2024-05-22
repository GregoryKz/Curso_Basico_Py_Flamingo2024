# Curso básico de Python
# Nome do Desenvolvedor: Gregory Klaus da Silva Pereira
# Versão: 1.0
# Exercício de Lógica de programação
# Com a linguagem de programação de Python
# Ler dois valores e imprimir uma das três mensagens a seguir: 
# ‘Números iguais’, caso os números sejam iguais 
# ‘Primeiro é maior’, caso o primeiro seja maior que o segundo; 
# ‘Segundo maior’, caso o segundo seja maior que o primeiro.

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
if valor1 == valor2:
    mensagem = "Números iguais"
elif valor1 > valor2:
    mensagem = "Primeiro é maior"
else:
    mensagem = "Segundo é maior"
print(mensagem)
print("Obrigado por utilizar nosso programa!")