package _java_jogo_da_velha;


public class Tabuleiro {

    public static final int X = 1;
    public static final int O = -1;
    public static final int Z = 0;

    public int[][] jogo;

    public Tabuleiro(int[][] jogo){
        this.jogo = jogo;
    }

    public int verificaGanhador(){
        for (int i = 0; i < 3; i++) {
            if (somaLinha(i) == 3){
                return X;
            } else if (somaLinha(i) == -3) {
                return O;
            }
        }
        return Z;
    }

    public int somaLinha(int linha) {
        return jogo[linha][0] + jogo[linha][1] + jogo[linha][2];
    }

}
