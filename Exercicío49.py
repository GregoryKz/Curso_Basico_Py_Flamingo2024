# Curso básico de Python
# Nome do Desenvolvedor: Gregory Klaus da Silva Pereira
# Versão: 1.0
# Exercício de Lógica de programação
# Com a linguagem de programação de Python
# Ler 3 valores (considere que não serão informados valores iguais) e escrever a soma dos 2 maiores.

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
valor3 = float(input("Digite o terceiro valor: "))
maior = max(valor1, valor2, valor3)
menor = min(valor1, valor2, valor3)
soma = valor1 + valor2 + valor3
segundo_maior = soma - maior - menor
print("A soma dos dois maiores valores é:", segundo_maior)
print("Obrigado por utilizar nosso programa!")