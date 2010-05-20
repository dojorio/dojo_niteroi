//To run tests execute:
//"export CLASSPATH=.:junit.jar"
//"javac *.java"
//"java junit.textui.TestRunner Teste"

import junit.framework.TestCase;

public class Teste extends TestCase {
	
	public void testSoma() {
		assertEquals(2, new Problema().soma(1,1));
	}

	public void testSomaFail() {
		assertEquals(3, new Problema().soma(1,1));
	}
}