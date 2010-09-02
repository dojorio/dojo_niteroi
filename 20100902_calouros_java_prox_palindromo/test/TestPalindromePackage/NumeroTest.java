package TestPalindromePackage;

import PalindromePackage.Numero;
import org.junit.After;
import org.junit.AfterClass;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Test;
import static org.junit.Assert.*;


public class NumeroTest {
    @Test
    public void testRecebe0Retorna1() {
        Numero instance = new Numero(0);
        assertEquals(1, instance.nextPalidrome());
    }
    
    @Test
    public void testRecebe1Retorna2() {
        Numero instance = new Numero(1);
        assertEquals(2, instance.nextPalidrome());
    }

    @Test
    public void testRecebe9Retorna11() {
        Numero instance = new Numero(9);
        assertEquals(11, instance.nextPalidrome());
    }

    @Test
    public void testRecebe11Retorna22() {
        Numero instance = new Numero(11);
        assertEquals(22, instance.nextPalidrome());
    }

    @Test
    public void testRecebe23Retorna33() {
        Numero instance = new Numero(23);
        assertEquals(33, instance.nextPalidrome());
    }

    @Test
    public void testeFuncaoIsPalindromeRetornaFalse() {
        Numero instance = new Numero(23);
        assertEquals(false, instance.isPalindrome());
    }

    @Test
    public void testeFuncaoIsPalindromeRetornaTrue() {
        Numero instance = new Numero(2);
        assertEquals(true, instance.isPalindrome());
    }
    @Test
    public void testeFuncaoIsPalindromeRetornaF() {
        Numero instance = new Numero(24567);
        assertEquals(false, instance.isPalindrome());
    }
}
