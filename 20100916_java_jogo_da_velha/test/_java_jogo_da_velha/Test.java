/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

package _java_jogo_da_velha;

import static org.junit.Assert.*;

/**
 *
 * @author bernardo
 */
public class Test extends {


    /**
     * Test of main method, of class Main.
     */
    @Test
    public void testXGanhaLinha1() {
        String[][] jogo = {{"x","x","x"},{"","o",""},{"o","",""}};

       assertEquals("x", Tabuleiro.verificaGanhador(jogo));
    }

}