# Curso básico de Python
# Nome do Desenvolvedor: Gregory Klaus da Silva Pereira
# Versão: 1.0
# Exercício de Lógica de programação
# Com a linguagem de programação de Python
# Ler o nome de 2 times e o número de gols marcados na partida (para cada time). Escrever o nome 
# do vencedor. Caso não haja vencedor deverá ser impressa a palavra EMPATE.

time1 = input("Digite o nome do time 1: ")
gols_time1 = int(input("Digite o número de gols do time 1: "))
time2 = input("Digite o nome do time 2: ")
gols_time2 = int(input("Digite o número de gols do time 2: "))
if gols_time1 > gols_time2:
    vencedor = time1
elif gols_time2 > gols_time1:
    vencedor = time2
else:
    vencedor = "EMPATE"
print("O vencedor da partida é:", vencedor)
print("Obrigado por utilizar nosso programa!")