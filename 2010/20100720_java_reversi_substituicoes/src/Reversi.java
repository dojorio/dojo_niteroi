

public class Reversi {

    public int[][] resultado(int[][] jogo, Jogada jogada){


        int[][] jogoResultado = jogo;
        jogoResultado[jogada.linha][jogada.coluna] = jogada.jogador;

        for (int i = jogada.linha-1; i>= 0;i--){
            if (jogoResultado[i][jogada.coluna] == jogada.jogador){
                break;
            }
            if (jogoResultado[i][jogada.coluna] == jogada.outroJogador()){
                jogoResultado[i][jogada.coluna] = jogada.jogador;
            }
            if (jogoResultado[i][jogada.coluna] == -1){
                for (int j = i+1; j<jogada.linha; j++){
                    jogoResultado[j][jogada.coluna] = jogada.outroJogador();
                }
                break;
            }
            


        }






        jogoResultado[jogada.linha][jogada.coluna] = jogada.jogador;
        if (jogada.jogador == 1)
            jogoResultado[jogada.linha - 1][jogada.coluna + 1] = jogada.jogador;
        else if (jogada.linha == 4)       
            jogoResultado[jogada.linha][jogada.coluna + 1] = jogada.jogador;

        return jogoResultado;
    }

}
