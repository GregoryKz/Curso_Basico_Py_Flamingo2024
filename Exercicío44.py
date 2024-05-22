#Curso basico de Python
#Nome do Densenvolvedor:Gregory Klaus da Silva Pereira
#Versão: 1.0
#Exercicio de Lógica de programação
#Com a linguagem de programaçãõ de python
# A jornada de trabalho semanal de um funcionário é de 40 horas. O funcionário que trabalhar mais 
# de 40 horas receberá hora extra, cujo cálculo é o valor da hora regular com um acréscimo de 50%. 
# Escreva um algoritmo que leia o número de horas trabalhadas em um mês, o salário por hora e escreva 
# o salário total do funcionário, que deverá ser acrescido das horas extras, caso tenham sido trabalhadas 
# (considere que o mês possua 4 semanas exatas).

horas_trabalhadas_mes = float(input("Digite o número de horas trabalhadas no mês: "))
salario_por_hora = float(input("Digite o salário por hora: "))

horas_semanais = 40
semanas_mes = 4
horas_mensal = horas_semanais * semanas_mes
valor_hora_extra = salario_por_hora * 1.5

if horas_trabalhadas_mes > horas_mensal:
    horas_extras = horas_trabalhadas_mes - horas_mensal
else:
    horas_extras = 0

salario_normal = min(horas_trabalhadas_mes, horas_mensal) * salario_por_hora
salario_extra = horas_extras * valor_hora_extra
salario_total = salario_normal + salario_extra

print(f"O salário total do funcionário é: R${salario_total:.2f}")
print("Obrigado.Volte Sempre")