
public class Jogada {
    public int jogador;
    public int linha;
    public int coluna;

    public Jogada(int jogador, int linha, int coluna){
        this.jogador = jogador;
        this.linha = linha;
        this.coluna = coluna;
    }

    public int outroJogador(){
        if (jogador == 1)
            return 0;
        else return 1;
    }

}
