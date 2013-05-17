package piratas;

/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
import org.junit.Test;
import static org.junit.Assert.*;

/**
 *
 * @author rodrigo
 */
public class PiratasTest {

    @Test
    public void teste1MoedaDe1Com1Pirata() {
        Piratas piratas = new Piratas();
        assertEquals(1, piratas.distribuir(new int[]{1, 0, 0, 0}, 1));
    }

    @Test
    public void teste2MoedasDe1Com1Pirata() {
        Piratas piratas = new Piratas();
        assertEquals(2, piratas.distribuir(new int[]{2, 0, 0, 0}, 1));
    }

    @Test
    public void teste1MoedaDe5Com1Pirata() {
        Piratas piratas = new Piratas();
        assertEquals(5, piratas.distribuir(new int[]{0, 0, 1, 0}, 1));
    }

    @Test
    public void teste1MoedaDe10Com1Pirata() {
        Piratas piratas = new Piratas();
        assertEquals(10, piratas.distribuir(new int[]{0, 0, 0, 1}, 1));
    }

    @Test
    public void teste1MoedaDe2Com1Pirata() {
        Piratas piratas = new Piratas();
        assertEquals(2, piratas.distribuir(new int[]{0, 1, 0, 0}, 1));
    }

    @Test
    public void teste2MoedaDe5Com1Pirata() {
        Piratas piratas = new Piratas();
        assertEquals(10, piratas.distribuir(new int[]{0, 0, 2, 0}, 1));
    }

    @Test
    public void teste1MoedaDe1E1MoedaDe2Com1Pirata() {
        Piratas piratas = new Piratas();
        assertEquals(3, piratas.distribuir(new int[]{1, 1, 0, 0}, 1));
    }

    @Test
    public void teste2MoedaDe1Com2Piratas() {
        Piratas piratas = new Piratas();
        assertEquals(1, piratas.distribuir(new int[]{2, 0, 0, 0}, 2));
    }

    @Test
    public void teste2MoedaDe2Com2Piratas() {
        Piratas piratas = new Piratas();
        assertEquals(2, piratas.distribuir(new int[]{0, 2, 0, 0}, 2));
    }

    @Test
    public void teste2MoedasDe5Com2Piratas() {
        Piratas piratas = new Piratas();
        assertEquals(5, piratas.distribuir(new int[]{0, 0, 2, 0}, 2));
    }

    @Test
    public void teste2MoedasDe10Com2Piratas() {
        Piratas piratas = new Piratas();
        assertEquals(10, piratas.distribuir(new int[]{0, 0, 0, 2}, 2));
    }

    @Test
    public void teste2MoedasDe1E1MoedaDe2Com2Piratas() {
        Piratas piratas = new Piratas();
        assertEquals(2, piratas.distribuir(new int[]{2, 1, 0, 0}, 2));
    }

    @Test
    public void teste10MoedasDe1E5MoedaDe2Com2Piratas() {
        Piratas piratas = new Piratas();
        assertEquals(10, piratas.distribuir(new int[]{10, 5, 0, 0}, 2));
    }

    @Test
    public void teste10MoedasDe1E2MoedasDe5E2MoedasDe10Com2Piratas() {
        Piratas piratas = new Piratas();
        assertEquals(15, piratas.distribuir(new int[]{10, 0, 2, 1}, 2));
    }

    @Test
    public void teste3MoedasDe1Com3Piratas() {
        Piratas piratas = new Piratas();
        assertEquals(1, piratas.distribuir(new int[]{3, 0, 0, 0}, 3));
    }

    @Test
    public void teste4MoedasDe1Com4Piratas() {
        Piratas piratas = new Piratas();
        assertEquals(1, piratas.distribuir(new int[]{4, 0, 0, 0}, 4));
    }

    @Test
    public void cantTeste3MoedasDe2E1MoedaDe10Com2Piratas() {
        Piratas piratas = new Piratas();
        assertEquals(-1, piratas.distribuir(new int[]{0, 3, 0, 1}, 2));
    }

    @Test
    public void teste3MoedasDe1E3MoedaDe2E3MoedasDe5Com2Piratas() {
        Piratas piratas = new Piratas();
        assertEquals(8, piratas.distribuir(new int[]{3, 3, 3, 0}, 3));
    }

@   Test
    public void teste1MoedasDe1E1MoedaDe2E3MoedasDe5Com3Piratas() {
        Piratas piratas = new Piratas();
        assertEquals(-1, piratas.distribuir(new int[]{1, 1, 3, 0}, 3));
    }
}
