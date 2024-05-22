#Curso basico de Python
#Nome do Densenvolvedor:Gregory Klaus da Silva Pereira
#Versão: 1.0
#Exercicio de Lógica de programação
#Escreva um algoritmo para ler o número total de eleitores de um município, o número de votos brancos, nulos e válidos. Calcular e escrever o percentual que cada um representa em relação ao total de eleitores.

print("Calculo dos votos")
total_de_votos=int(input("Digite a quantidade total de votos: "))
votos_brancos=int(input("Digite quantos votos branco teve: "))
votos_nulos=int(input("Digite quantos votos nulos teve:  "))
votos_valios=int(input("Digite a quantidade de votos validos: "))
if votos_brancos+votos_nulos+votos_valios!=total_de_votos:
    print("A quantidade de votos não corresponde ao total de votos.")
else:
    percentual_branco=(votos_brancos/total_de_votos)*100
    percentual_nulos=(votos_nulos/total_de_votos)*100
    percentual_validos=(votos_valios/total_de_votos)*100
print(f"O percentual de votos Branco é {percentual_branco  :.2f}%")
print(f"O percentual de votos Nulos é {percentual_nulos  :.2f}%")
print(f"O percentual de votos Validos é {percentual_validos  :.2f}%")
print("Obrigado. Volte Sempre")