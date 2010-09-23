package _java_jogo_da_velha;

import org.junit.Test;
import static org.junit.Assert.*;


public class teste_jogodavelha {

    public static final int X = Tabuleiro.X;
    public static final int O = Tabuleiro.O;
    public static final int Z = Tabuleiro.Z;
    
    @Test
    public void testeXGanhaNaPrimeiraLinha()
    {
        int[][] jogo = {{ X, X, X}, {Z, O, Z}, {O, Z, Z}};
        
        assertEquals(X, new Tabuleiro(jogo).verificaGanhador());
    }

    @Test
    public void testeOGanhaNaPrimeiraLinha()
    {
        int[][] jogo = {{O, O, O}, {Z, X, Z}, {X, Z, Z}};
        assertEquals(O, new Tabuleiro(jogo).verificaGanhador());
    }

    @Test
    public void testeXGanhaNaSegundaLinha()
    {
        int[][] jogo = {{O, X, O}, {X, X, X}, {O, Z, Z}};
        assertEquals(X, new Tabuleiro(jogo).verificaGanhador());
    }

    @Test
    public void testeOGanhaNaSegundaLinha()
    {
        int[][] jogo = {{X, X, Z}, {O, O, O}, {O, Z, X}};
        assertEquals(O, new Tabuleiro(jogo).verificaGanhador());
    }

    @Test
    public void testeXGanhaNaTerceiraLinha()
    {
        int[][] jogo = {{O, X, Z}, {O, Z, O}, {X, X, X}};
        assertEquals(X, new Tabuleiro(jogo).verificaGanhador());
    }


}
