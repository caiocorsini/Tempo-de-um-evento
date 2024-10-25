QUANT_SEGUNDOS_DIA = 86400
QUANT_SEGUNDOS_HORA = 3600
QUANT_SEGUNDOS_MINUTO = 60


dia_ini_string = input()
horario_ini_string = input()
dia_fim_string = input()
horario_fim_string = input()

split_aux = dia_ini_string.split(" ")
dia_ini = int(split_aux[1])
split_aux = dia_fim_string.split(" ")
dia_fim = int(split_aux[1])

split_aux = horario_ini_string.split(" ")
hora_ini = int(split_aux[0])
minuto_ini = int(split_aux[2])
segundo_ini = int(split_aux[4])

split_aux = horario_fim_string.split(" ")
hora_fim = int(split_aux[0])
minuto_fim = int(split_aux[2])
segundo_fim = int(split_aux[4])

quant_seg_ini = QUANT_SEGUNDOS_DIA * dia_ini + QUANT_SEGUNDOS_HORA * hora_ini + QUANT_SEGUNDOS_MINUTO * minuto_ini + segundo_ini
quant_seg_fim = QUANT_SEGUNDOS_DIA * dia_fim + QUANT_SEGUNDOS_HORA * hora_fim + QUANT_SEGUNDOS_MINUTO * minuto_fim + segundo_fim
quant_seg_total = quant_seg_fim - quant_seg_ini

quant_dias = 0
quant_horas = 0
quant_minutos = 0
quant_segundos = 0

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
