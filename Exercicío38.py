#Curso basico de Python
#Nome do Densenvolvedor:Gregory Klaus da Silva Pereira
#Versão: 1.0
#Exercicio de Lógica de programação
#Com a linguagem de programaçãõ de python
# Ler dois valores (considere que não serão lidos valores iguais) e escrevê-los em ordem crescente

print("Digite dois numeros que irei colocar em ordem crescente")
numero1=int(input("Digite um numero: "))
numero2=int(input("Digite outro numero: "))
if numero1<numero2:
    print(f"A ordem crescente é {numero1},{numero2} ")
else:
    print(f"A ordem crescente é {numero2}, {numero1} ")
print("Obrigado")