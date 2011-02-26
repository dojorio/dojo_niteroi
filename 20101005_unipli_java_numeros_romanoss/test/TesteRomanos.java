import org.junit.Test;
import org.junit.Assert;
import org.junit.internal.builders.NullBuilder;

public class TesteRomanos {

    @Test
    public void romanoIretorna1() {
        NumeroRomano numeroRomano = new NumeroRomano("I");
        Assert.assertEquals(1, numeroRomano.paraInteiro());
    }

    @Test
    public void romanoIIretorna2() {
        NumeroRomano numeroRomano = new NumeroRomano("II");
        Assert.assertEquals(2, numeroRomano.paraInteiro());
    }

    @Test
    public void romanoIIIretorna3() {
        NumeroRomano numeroRomano = new NumeroRomano("III");
        Assert.assertEquals(3, numeroRomano.paraInteiro());
    }

    @Test
    public void romanoVretorna5() {
        NumeroRomano numeroRomano = new NumeroRomano("V");
        Assert.assertEquals(5, numeroRomano.paraInteiro());
    }

    @Test
    public void romanoVIretorna6() {
        NumeroRomano numeroRomano = new NumeroRomano("VI");
        Assert.assertEquals(6, numeroRomano.paraInteiro());
    }

    @Test
    public void romanoVIIretorna7() {
        NumeroRomano numeroRomano = new NumeroRomano("VII");
        Assert.assertEquals(7, numeroRomano.paraInteiro());
    }

}