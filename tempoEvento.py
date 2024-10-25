# Constantes de quantidades de segundos
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
# Horário de início
split_aux = horario_ini_string.split(" : ") # 08 : 30 : 40 -> ["08", "30", "40"]
hora_ini = int(split_aux[0])
minuto_ini = int(split_aux[1])
segundo_ini = int(split_aux[2])

# Horário de fim
split_aux = horario_fim_string.split(" : ")
hora_fim = int(split_aux[0])
minuto_fim = int(split_aux[1])
segundo_fim = int(split_aux[2])

# Somando as quantidades de segundos no total para início e para fim
quant_seg_ini = total_segundos(dia_ini, hora_ini, minuto_ini, segundo_ini)
quant_seg_fim = total_segundos(dia_fim, hora_fim, minuto_fim, segundo_fim)
quant_seg_total = quant_seg_fim - quant_seg_ini  # Diferença em segundos de fim e início

quantidades = [0,0,0,0]
valores = [QUANT_SEGUNDOS_DIA, QUANT_SEGUNDOS_HORA, QUANT_SEGUNDOS_MINUTO, 1]
i = 0

while quant_seg_total > 0:
    #print(quant_seg_total)
    if valores[i] <= quant_seg_total:
        quant_seg_total -= valores[i]
        quantidades[i] += 1
    else:
        i += 1

print(f"{quantidades[0]} dia(s)\n{quantidades[1]} hora(s)\n{quantidades[2]} minuto(s)\n{quantidades[3]} segundo(s)")
