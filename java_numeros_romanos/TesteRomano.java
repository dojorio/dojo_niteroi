
import dojo.Romano;
import org.junit.Test;
import static org.junit.Assert.*;

public class TesteRomano {

    public Romano conversor = new Romano();

    
    @Test
    public void teste1RetornaI() {
        assertEquals("I", conversor.converteDeInteiro(1));
    }

    @Test
    public void teste2RetornaII() {
        assertEquals("II", conversor.converteDeInteiro(2));
    }

    @Test
    public void teste3RetornaIII() {
        assertEquals("III", conversor.converteDeInteiro(3));
    }

    @Test
    public void teste4RetornaIV() {
        assertEquals("IV", conversor.converteDeInteiro(4));
    }

    @Test
    public void teste5RetornaV() {
        assertEquals("V", conversor.converteDeInteiro(5));
    }

    @Test
    public void teste6RetornaVI() {
        assertEquals("VI", conversor.converteDeInteiro(6));
    }

    @Test
    public void teste7RetornaVII() {
        assertEquals("VII", conversor.converteDeInteiro(7));
    }

    @Test
    public void teste9RetornaIX() {
        assertEquals("IX", conversor.converteDeInteiro(9));
    }

    @Test
    public void teste10RetornaX() {
        assertEquals("X", conversor.converteDeInteiro(10));
    }

    @Test
    public void teste11RetornaXI() {
        assertEquals("XI", conversor.converteDeInteiro(11));
    }

    @Test
    public void teste15RetornaXV() {
        assertEquals("XV", conversor.converteDeInteiro(15));
    }


    @Test
    public void teste16RetornaXVI() {
        assertEquals("XVI", conversor.converteDeInteiro(16));
    }

    @Test
    public void teste19RetornaXIX() {
        assertEquals("XIX", conversor.converteDeInteiro(19));
    }

    @Test
    public void teste20RetornaXX() {
        assertEquals("XX", conversor.converteDeInteiro(20));
    }


    @Test
    public void teste21RetornaXXI() {
        assertEquals("XXI", conversor.converteDeInteiro(21));
    }

    @Test
    public void teste39RetornaXXXIX() {
        assertEquals("XXXIX", conversor.converteDeInteiro(39));
    }

    @Test
    public void teste40RetornXL() {
        assertEquals("XL", conversor.converteDeInteiro(40));
    }

    @Test
    public void teste41RetornXLI() {
        assertEquals("XLI", conversor.converteDeInteiro(41));
    }

    @Test
    public void teste49RetornXLIX() {
        assertEquals("XLIX", conversor.converteDeInteiro(49));
    }
}

