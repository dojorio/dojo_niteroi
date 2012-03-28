import aipaladino.Foe;
import aipaladino.Paladin;
import org.junit.Test;
import org.junit.Before;
import static org.junit.Assert.*;

public class AiPaladinoTest {
    Paladin arthas;
    Foe illidan;
            
    @Before
    public void setUp() {
        arthas = new Paladin(100);
        illidan = new Foe(100);
    }

    @Test
    public void testPaladinAndFoe100HpShouldBuff() {
        assertEquals("buff", arthas.ai(illidan));
    }
    
    @Test
    public void testPaladinBuffedAndAllFull(){
        arthas.buff();
        assertEquals("pow", arthas.ai(illidan));
    }
            
    @Test
    public void testPaladinFucked() {
        arthas.setHp(20);
        assertEquals("cure", arthas.ai(illidan));
    }
    
    @Test
    public void testPaladinHeals40() {
        arthas.setHp(20);
        arthas.cure();
        assertEquals(60, arthas.getHp());
    }
    
    @Test
    public void testPaladinFuckedAndFoeFuckederPow() {
        arthas.setHp(20);
        illidan.setHp(1);
        arthas.buff();
        assertEquals("pow", arthas.ai(illidan));
    }
    
    @Test
    public void testPaladinPowDealsDamage(){
        arthas.pow(illidan);
        assertEquals(85, illidan.getHp());
    }
    
    @Test
    public void testHpCantBeNegative(){
        illidan.setHp(9);
        arthas.pow(illidan);
        assertEquals(0, illidan.getHp());
    }
}
