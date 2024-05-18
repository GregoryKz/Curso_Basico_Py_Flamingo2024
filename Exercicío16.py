#Curso basico de Python
#Nome do Densenvolvedor:Gregory Klaus da Silva Pereira
#Versão: 1.0
#Exercicio de Lógica de programação
#Com a linguagem de programaçãõ de python
#Exercicio de IMC
#Calculo do Indice de massa corporal

print("Calcule seu IMC")
altura=float(input("Digite sua altura em centimetros: "))
peso=float(input("Digite seu peso em quilogramasa: "))
imc=peso/(altura**altura)/100
print("Calculando imc....")
if imc<18.0:
    print("Voce está abaixo do peso ideal!")
elif imc>=18.5 and imc<24.9:
    print("Você está no peso ideal.")
elif imc>=25.0 and imc<30.0:
    print("Você esta com sobrepeso")
else:
    print("Você está obeso!!")
print("Obrigado.Volte Sempre...")

