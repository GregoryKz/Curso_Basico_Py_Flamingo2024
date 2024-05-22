#Curso basico de Python
#Nome do Densenvolvedor:Gregory Klaus da Silva Pereira
#Versão: 1.0
#Exercicio de Lógica de programação
#Com a linguagem de programaçãõ de python
# Ler a hora de início e a hora de fim de um jogo de Xadrez (considere apenas horas inteiras, sem os 
# minutos) e calcule a duração do jogo em horas, sabendo-se que o tempo máximo de duração do jogo é 
# de 24 horas e que o jogo pode iniciar em um dia e terminar no dia seguinte

hora_inicio = int(input("Digite a hora de início do jogo (0-23): "))
hora_fim = int(input("Digite a hora de fim do jogo (0-23): "))

if 0 <= hora_inicio < 24 and 0 <= hora_fim < 24:
    if hora_fim >= hora_inicio:
        duracao = hora_fim - hora_inicio
    else:
        duracao = (24 - hora_inicio) + hora_fim
    print(f"A duração do jogo é de {duracao} horas.")
else:
    print("As horas de início e fim devem estar no intervalo de 0 a 23.")
print("Obrigado por usar o programa")