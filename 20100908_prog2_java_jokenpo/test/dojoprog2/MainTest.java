package dojoprog2;

import org.junit.Test;
import static org.junit.Assert.*;

public class MainTest
{

    @Test
    public void testTesouraPapelGanhaTesoura()
    {
        assertEquals(new Jokenpo().jogar("tesoura", "papel"), "tesoura");
    }
    @Test
    public void testTesouraTesouraEmpate()
    {
        assertEquals(new Jokenpo().jogar("tesoura", "tesoura"), "empate");
    }
    @Test
    public void testPedraPapelGanhaPapel()
    {
        assertEquals(new Jokenpo().jogar("pedra", "papel"), "papel");
    }
    @Test
    public void testPedraTesouraGanhaPedra()
    {
        assertEquals(new Jokenpo().jogar("pedra", "tesoura"), "pedra");
    }
    @Test
    public void testTesouraPedraGanhaPedra()
    {
        assertEquals(new Jokenpo().jogar("tesoura", "pedra"), "pedra");
    }
    @Test
    public void testPapelPedraGanhaPapel()
    {
        assertEquals(new Jokenpo().jogar("papel", "pedra"), "papel");
    }
    @Test
    public void testPapelTesouraGanhaTesoura()
    {
        assertEquals(new Jokenpo().jogar("papel", "tesoura"), "tesoura");
    }

}