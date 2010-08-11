import junit.framework.*;


public class TesteReversi extends TestCase{



    void defineJogo(int[][] matriz){
        for(int linha = 0;linha<matriz.length;linha++)
            for(int coluna = linha;coluna<matriz.length;coluna++)
                matriz[linha][coluna] = -1;
    }

    boolean compararMatriz(int[][] matriz1,int[][] matriz2){
        for(int linha = 0;linha<matriz1.length;linha++)
            for(int coluna = 0;coluna<matriz1.length;coluna++)
                if (matriz1[linha][coluna] != matriz2[linha][coluna])
                    return false;
        return true;
    }

    public void testReversiInicioJogoOcomecaEm_4_2(){
        int[][] jogo = {{-1,-1,-1,-1,-1,-1,-1,-1},
                        {-1,-1,-1,-1,-1,-1,-1,-1},
                        {-1,-1,-1,-1,-1,-1,-1,-1},
                        {-1,-1,-1, 0, 1,-1,-1,-1},
                        {-1,-1,-1, 1, 0,-1,-1,-1},
                        {-1,-1,-1,-1,-1,-1,-1,-1},
                        {-1,-1,-1,-1,-1,-1,-1,-1},
                        {-1,-1,-1,-1,-1,-1,-1,-1},
        };

        Jogada jogada = new Jogada(0, 4 ,2);

        int[][] jogoResultado = {{-1,-1,-1,-1,-1,-1,-1,-1},
                        {-1,-1,-1,-1,-1,-1,-1,-1},
                        {-1,-1,-1,-1,-1,-1,-1,-1},
                        {-1,-1,-1, 0, 1,-1,-1,-1},
                        {-1,-1, 0, 0, 0,-1,-1,-1},
                        {-1,-1,-1,-1,-1,-1,-1,-1},
                        {-1,-1,-1,-1,-1,-1,-1,-1},
                        {-1,-1,-1,-1,-1,-1,-1,-1},
        };
        if (compararMatriz(new Reversi().resultado(jogo, jogada),jogoResultado))
            assertEquals(true, true);
        else assertEquals(false, true);
    }

    public void testReversiResultadoAnteriorFazDiagonalCom1(){
        int[][] jogo = {{-1,-1,-1,-1,-1,-1,-1,-1},
                        {-1,-1,-1,-1,-1,-1,-1,-1},
                        {-1,-1,-1,-1,-1,-1,-1,-1},
                        {-1,-1,-1, 0, 1,-1,-1,-1},
                        {-1,-1, 0, 0, 0,-1,-1,-1},
                        {-1,-1,-1,-1,-1,-1,-1,-1},
                        {-1,-1,-1,-1,-1,-1,-1,-1},
                        {-1,-1,-1,-1,-1,-1,-1,-1},
        };

        Jogada jogada = new Jogada(1,5,2);

        int[][] jogoResultado = {{-1,-1,-1,-1,-1,-1,-1,-1},
                                {-1,-1,-1,-1,-1,-1,-1,-1},
                                {-1,-1,-1,-1,-1,-1,-1,-1},
                                {-1,-1,-1, 0, 1,-1,-1,-1},
                                {-1,-1, 0, 1, 0,-1,-1,-1},
                                {-1,-1, 1,-1,-1,-1,-1,-1},
                                {-1,-1,-1,-1,-1,-1,-1,-1},
                                {-1,-1,-1,-1,-1,-1,-1,-1},
        };

        if (compararMatriz(new Reversi().resultado(jogo, jogada),jogoResultado))
            assertEquals(true, true);
        else assertEquals(false, true);
    }

    public void testReversiContinuaCom(){
        int[][] jogo = {{-1,-1,-1,-1,-1,-1,-1,-1},
                        {-1,-1,-1,-1,-1,-1,-1,-1},
                        {-1,-1,-1,-1,-1,-1,-1,-1},
                        {-1,-1,-1, 0, 1,-1,-1,-1},
                        {-1,-1, 0, 1, 0,-1,-1,-1},
                        {-1,-1, 1,-1,-1,-1,-1,-1},
                        {-1,-1,-1,-1,-1,-1,-1,-1},
                        {-1,-1,-1,-1,-1,-1,-1,-1},
        };

        Jogada jogada = new Jogada(0,5,3);

        int[][] jogoResultado = {{-1,-1,-1,-1,-1,-1,-1,-1},
                                {-1,-1,-1,-1,-1,-1,-1,-1},
                                {-1,-1,-1,-1,-1,-1,-1,-1},
                                {-1,-1,-1, 0, 1,-1,-1,-1},
                                {-1,-1, 0, 0, 0,-1,-1,-1},
                                {-1,-1, 1, 0,-1,-1,-1,-1},
                                {-1,-1,-1,-1,-1,-1,-1,-1},
                                {-1,-1,-1,-1,-1,-1,-1,-1},
        };

        if (compararMatriz(new Reversi().resultado(jogo, jogada),jogoResultado))
            assertEquals(true, true);
        else assertEquals(false, true);
    }
}