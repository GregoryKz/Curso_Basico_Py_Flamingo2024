#Curso basico de Python
#Nome do Densenvolvedor:Gregory Klaus da Silva Pereira
#Versão: 1.0
#Exercicio de Lógica de programação
#Com a linguagem de programaçãõ de python
# Faça um algoritmo para ler: número da conta do cliente, saldo, débito e crédito. Após, calcular e escrever o saldo atual
# Também testar se saldo atual for maior ou igual a zero escrever a mensagem 'Saldo Positivo', senão escrever a mensagem 'Saldo Negativo'.
print("Conta extrato bancario")
saldo=float(input("Digite o saldo da sua conta: "))
debito=float(input("Digite o quanto gastou no cartão de debito: "))
credito=float(input("Digite quanto você ira receber : "))
saldo_atual=saldo-debito+credito
if saldo_atual>=0:
    print(f"O seu saldo é de R$:{saldo_atual:.2f}")
    print("Seu saldo esta positivo.Parabéns Você é controlado")
else:
    print(f"Seu saldo e de R$:{saldo_atual:.2f}")
    print("Seu saldo esta negativo!!. Tem que ser controlar mais")
print("Obrigado")