// Beecrowd - Problema 1061 - Tempo de um Evento
// Autor: Caio Vinicius Corsini Filho

import java.util.Scanner;
public class Main {
    // Constantes de quantidades de segundos
    // Escolhi converter tudo especificamente para segundos para não ter que trabalhar com floats
    static int QUANT_SEGUNDOS_DIA = 86400;
    static int QUANT_SEGUNDOS_HORA = 3600;
    static int QUANT_SEGUNDOS_MINUTO = 60;

    // Função para somar total de segundos em dados dias, horas, minutos e segundos
    public static int totalSegundos(int dias, int horas, int minutos, int segundos){
        return (QUANT_SEGUNDOS_DIA * dias +
                 QUANT_SEGUNDOS_HORA * horas +
                 QUANT_SEGUNDOS_MINUTO * minutos +
                 segundos);
    }

    public static void main(String[] args) {
        Scanner inputUser = new Scanner(System.in);  // Para pegar inputs do usuario


        // Todos os inputs que o usuário vai dar
        String diaIniString = inputUser.nextLine();
        String horarioIniString = inputUser.nextLine();
        String diaFimString = inputUser.nextLine();
        String horarioFimString = inputUser.nextLine();


        // PROCESSAMENTO DE INPUTS: Como todos os inputs vem na forma de strings, preciso extrair os inteiros delas.
        // Uso função split(<token>) a qual converte uma string em uma lista usando um <token> como separador
        // Processando dias
        String[] splitAux = diaIniString.split(" ");  // "Dia 5" -> ["Dia", "5"]
        int diaIni = Integer.parseInt(splitAux[1]);
        splitAux = diaFimString.split(" ");
        int diaFim = Integer.parseInt(splitAux[1]);


        // Processando horários
        // Ainda estão como strings, precisa converter para int para fazer os cálculos
        // EXEMPLO CONVERSÃO - 08 : 30 : 40 -> ["08", "30", "40"]
        // Horario de início
        splitAux = horarioIniString.split(" : ");
        int horaIni = Integer.parseInt(splitAux[0]);
        int minutoIni = Integer.parseInt(splitAux[1]);
        int segundoIni = Integer.parseInt(splitAux[2]);

        // Horario de Fim
        splitAux = horarioFimString.split(" : ");
        int horaFim = Integer.parseInt(splitAux[0]);
        int minutoFim = Integer.parseInt(splitAux[1]);
        int segundoFim = Integer.parseInt(splitAux[2]);


        // Somando as quantidades de segundos no total para início e para fim
        int quantSegIni = totalSegundos(diaIni, horaIni, minutoIni, segundoIni);
        int quantSegFim = totalSegundos(diaFim, horaFim, minutoFim, segundoFim);
        int quantSegTotal = quantSegFim - quantSegIni;  // Diferença em segundos de fim e início
        
        int[] quantidades = {0,0,0,0};  // Vetor auxiliar para armazenar quantidades de dias, horas, minutos e segundos respectivamente
        int[] valores = {QUANT_SEGUNDOS_DIA, QUANT_SEGUNDOS_HORA, QUANT_SEGUNDOS_MINUTO, 1};
        int i=0;  // Variável contadora auxiliar para determinar o que usar: dia, hora, minuto ou segundo (vetor logo acima)

        while(quantSegTotal > 0){
            if(valores[i] <= quantSegTotal){
                quantSegTotal -= valores[i];
                quantidades[i]++;
            } else i++;
        }

        // Impressao formatada do resultado
        System.out.printf("%d dia(s)\n%d hora(s)\n%d minuto(s)\n%d segundo(s)\n", quantidades[0], quantidades[1], quantidades[2], quantidades[3]);
    }
}

/*
PONTOS IMPORTANTES
1. Quem tiver curiosidade, observar algoritmo guloso do "problema do troco", o qual usa uma estratégia similar
*/