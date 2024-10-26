**Inteiro** *Dia Início*, *Horário Início* <- lerDoUsuario <br>
**Inteiro** *Dia Fim*, *Horário Fim* <- lerDoUsuario

**Inteiro** *Horas início*, *Minutos Início*, *Segundos Início* <- mapear(*Horário Início*) <br>
**Inteiro** *Horas Fim*, *Minutos Fim*, *Segundos Fim* <- mapear(*Horário Fim*)

**Inteiro** *Total segundos início* <- <br>
&nbsp;&nbsp;&nbsp;&nbsp;*Horas início* x 86400 + <br>
&nbsp;&nbsp;&nbsp;&nbsp;*Minutos Início* x 3600 + <br>
&nbsp;&nbsp;&nbsp;&nbsp;*Segundos Início* <br>

**Inteiro** *Total segundos Fim* <- <br>
&nbsp;&nbsp;&nbsp;&nbsp;*Horas Fim* x 86400 + <br>
&nbsp;&nbsp;&nbsp;&nbsp;*Minutos Fim* x 3600 + <br>
&nbsp;&nbsp;&nbsp;&nbsp;*Segundos Fim* <br>

**Inteiro** *Total Segundos* <- *Total segundos Fim* - *Total segundos início*  

**Lista de Inteiros** *quantidades* <- [0, 0, 0, 0]  
**Lista de Inteiros** *valores* <- [*86400*, *3600*, *60*, 1]  
**Inteiro** *i* <- 0  

Enquanto *Total Segundos* for maior que 0  
&nbsp;&nbsp;&nbsp;&nbsp; Se *valores*[i] for menor ou igual a *quant_seg_total*  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *Total Segundos* <- *Total Segundos* - *valores*[i]  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *quantidades*[i] <- incrementar *quantidades*[i]  
&nbsp;&nbsp;&nbsp;&nbsp; Senão  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; decrementar i  

Imprimir (*quantidades*[0], "dia(s)")  
Imprimir (*quantidades*[1], "hora(s)")  
Imprimir (*quantidades*[2], "minuto(s)")  
Imprimir (*quantidades*[3], "segundo(s)")  
