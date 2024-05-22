# Curso básico de Python
# Nome do Desenvolvedor: Gregory Klaus da Silva Pereira
# Versão: 1.0
# Exercício de Lógica de programação
# Com a linguagem de programação de Python
# Faça um algoritmo para ler: número da conta do cliente, saldo, débito e crédito. Após, calcular e 
# escrever o saldo atual (saldo atual = saldo - débito + crédito). Também testar se saldo atual for maior 
# ou igual a zero escrever a mensagem 'Saldo Positivo', senão escrever a mensagem 'Saldo Negativo'.

numero_conta = input("Digite o número da conta do cliente: ")
saldo = float(input("Digite o saldo da conta: "))
debito = float(input("Digite o débito da conta: "))
credito = float(input("Digite o crédito da conta: "))
saldo_atual = saldo - debito + credito
if saldo_atual >= 0:
    mensagem = "Saldo Positivo"
else:
    mensagem = "Saldo Negativo"

print("O saldo atual da conta é:", saldo_atual)
print("Situação da conta:", mensagem)
print("Obrigado por utilizar nosso programa!")