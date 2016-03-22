
import junit.framework.TestCase;

public class TesteRomanos extends TestCase{
	
	public void test1RetornaI(){
		assertEquals("I", new NumerosRomanos().paraInteiro(1));
	}
	
	public void test2RetornaII(){
		assertEquals("II", new NumerosRomanos().paraInteiro(2));
	}
	
	public void test3RetornaIII(){
		assertEquals("III", new NumerosRomanos().paraInteiro(3));
	}
	
	public void test4RetornaIV(){
		assertEquals("IV", new NumerosRomanos().paraInteiro(4));
	}

	public void test5RetornaV(){
		assertEquals("V", new NumerosRomanos().paraInteiro(5));
	}
	
	public void test6RetornaVI(){
		assertEquals("VI", new NumerosRomanos().paraInteiro(6));
	}	
}