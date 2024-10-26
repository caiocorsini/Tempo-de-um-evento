# Beecrowd - Problema 1061 - Tempo de um Evento
# Autor: Caio Vinicius Corsini Filho

# Constantes de quantidades de segundos
# Escolhi converter tudo especificamente para segundos para não ter que trabalhar com floats
QUANT_SEGUNDOS_DIA = 86400
QUANT_SEGUNDOS_HORA = 3600
QUANT_SEGUNDOS_MINUTO = 60

# Função para somar total de segundos em dados dias, horas, minutos e segundos
def total_segundos(dias, horas, minutos, segundos):
    return (QUANT_SEGUNDOS_DIA * dias +
                 QUANT_SEGUNDOS_HORA * horas +
                 QUANT_SEGUNDOS_MINUTO * minutos +
                 segundos)

# Todos os inputs que o usuário vai dar
dia_ini_string = input()
horario_ini_string = input()
dia_fim_string = input()
horario_fim_string = input()

# PROCESSAMENTO DE INPUTS: Como todos os inputs vem na forma de strings, preciso extrair os inteiros delas.
# Uso função split(<token>) a qual converte uma string em uma lista usando um <token> como separador
# Processando dias
split_aux = dia_ini_string.split(" ") # "Dia 5" -> ["Dia", "5"]
dia_ini = int(split_aux[1])
split_aux = dia_fim_string.split(" ")
dia_fim = int(split_aux[1])

# Processando horários
# Ainda estão como strings, precisa converter para int para fazer os cálculos
# EXEMPLO CONVERSÃO - 08 : 30 : 40 -> [8, 3, 4]
# Horário de início
hora_ini, minuto_ini, segundo_ini = map(int, horario_ini_string.split(" : "))

# Horário de fim
hora_fim, minuto_fim, segundo_fim = map(int, horario_fim_string.split(" : "))

# Somando as quantidades de segundos no total para início e para fim
quant_seg_ini = total_segundos(dia_ini, hora_ini, minuto_ini, segundo_ini)
quant_seg_fim = total_segundos(dia_fim, hora_fim, minuto_fim, segundo_fim)
quant_seg_total = quant_seg_fim - quant_seg_ini  # Diferença em segundos de fim e início

quantidades = [0,0,0,0]  # Vetor auxiliar para armazenar quantidades de dias, horas, minutos e segundos respectivamente
valores = [QUANT_SEGUNDOS_DIA, QUANT_SEGUNDOS_HORA, QUANT_SEGUNDOS_MINUTO, 1]
i = 0  # Variável contadora auxiliar para determinar o que usar: dia, hora, minuto ou segundo (vetor logo acima)

# Vou diminuindo a quant de segundos com o máximo de dias que puder, depois horas, depois minutos e depois segundos
while quant_seg_total > 0:  # Vai diminuindo até não sobrarem mais segundos
    if valores[i] <= quant_seg_total:
        quant_seg_total -= valores[i]
        quantidades[i] += 1
    else:
        i += 1 # Passo a usar outro valor para diminuir a quantidade de segundos restante

# Impressão formatada do resultado
print(f"{quantidades[0]} dia(s)\n{quantidades[1]} hora(s)\n{quantidades[2]} minuto(s)\n{quantidades[3]} segundo(s)")

'''
PONTOS IMPORTANTES
1. Quem tiver curiosidade, observar algoritmo guloso do "problema do troco", o qual usa uma estratégia similar
'''
