#Curso basico de Python
#Nome do Densenvolvedor:Gregory Klaus da Silva Pereira
#Versão: 1.0
#Exercicio de Lógica de programação
#Com a linguagem de programaçãõ de python
#Ler o ano atual e o ano de nascimento de uma pessoa. Escrever uma mensagem que diga se ela poderá ou não votar este ano (não é necessário considerar o mês em que a pessoa nasceu).
print("Você pode votar ?")
ano_nasceu=int(input("Digite o ano que nasceu: "))
ano_atual=2024
idade=ano_nasceu-ano_atual
if idade<16:
    print("Você não pode votar! em 2024. Sinto muito")
else:
    print("Você pode votar! em 2024. Seje consiente com o seu voto")
print("Obrigado. Boa eleições")