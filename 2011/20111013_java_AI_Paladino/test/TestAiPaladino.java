import AIPaladino.Ally;
import AIPaladino.Battlefield;
import AIPaladino.Enemy;
import AIPaladino.Paladin;
import org.junit.Test;
import static org.junit.Assert.*;
import org.junit.Before;
import AIPaladino.PallyAI;

public class TestAiPaladino {

    public PallyAI ai;
    public Battlefield bf;
    public Paladin pally;
    public Ally ally;
    public Enemy enemy;

    @Before
    public void before(){
        
        this.enemy = new Enemy();
        this.ally = new Ally();
        this.pally = new Paladin();
        this.bf = new Battlefield(enemy, ally, pally);
        this.ai = new PallyAI(bf);

    }

    @Test
    public void testInicioFazBuff() {
       
        assertEquals("buff", this.ai.action());
          
    }

    @Test
    public void testPaladinoVidaBaixaCuraSelf() {

        this.pally.setHp(25);
        assertEquals("cura self", this.ai.action());

    }


    @Test
    public void testPalladinoCuraAllyVidaBaixa() {

      this.ally.setHp(25);
      assertEquals("cura ally", this.ai.action());

    }

}
