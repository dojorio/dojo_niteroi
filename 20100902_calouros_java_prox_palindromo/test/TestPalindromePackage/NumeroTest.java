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
    public void testNextPalidrome() {
        Numero instance = new Numero();
        assertEquals(0, instance.nextPalidrome());
    }

}