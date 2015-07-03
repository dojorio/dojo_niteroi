import happynumbers.HappyNumber;
import org.junit.After;
import org.junit.AfterClass;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Test;
import static org.junit.Assert.*;


public class TestHappyNumbers {
    
    @Test
    public void numero1feliz() {
        assertTrue(new HappyNumber(1).isHappy());
    }
    
    @Test
    public void numero10feliz() {
        assertTrue(new HappyNumber(10).isHappy());
    }
    
    @Test
    public void numero2triste() {
        assertFalse(new HappyNumber(2).isHappy());
    }
    
    @Test
    public void numero100feliz(){
        assertTrue(new HappyNumber(100).isHappy());
    }
    
    @Test
    public void numero130feliz(){
        assertTrue(new HappyNumber(130).isHappy());
    }
    
    @Test
    public void numero1000feliz(){
        assertTrue(new HappyNumber(1000).isHappy());
    }
    
    
}