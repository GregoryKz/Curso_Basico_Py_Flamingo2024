#Curso basico de Python
#Nome do Densenvolvedor:Gregory Klaus da Silva Pereira
#Versão: 1.0
#Exercicio de Lógica de programação
#Com a linguagem de programaçãõ de python
#Exercicio dos numeros primos

print("Numeros primos ")
numero = int(input("Digite um numero, que eu irei dizer se ele é primo: "))
primo = True

if numero <= 1:
    primo = False
else:
    for i in range(2, numero):
        if numero % i == 0:
            primo = False
            break

if primo and numero > 1:
    print(numero, "é um número primo.")
else:
    print(numero, "não é um número primo.")
print("Obrigado por usar o programa. ;)")