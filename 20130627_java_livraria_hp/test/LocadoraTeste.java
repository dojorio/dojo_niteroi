/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */



import org.junit.After;
import org.junit.AfterClass;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Test;
import static org.junit.Assert.*;

/**
 *
 * @author rodcastro
 */
public class LocadoraTeste {

    public LocadoraTeste() {
    }

    @BeforeClass
    public static void setUpClass() throws Exception {
    }

    @AfterClass
    public static void tearDownClass() throws Exception {
    }

    @Before
    public void setUp() {
    }

    @After
    public void tearDown() {
    }

    /**
     * Test of doTest method, of class Teste.
     */
    @Test
    public void test0LivrosPreco0() {
        double expectedPrice = 0;
        double preco = Locadora.comprarLivros(null);
        assertEquals(expectedPrice, preco, 0.001);
    }

    @Test
    public void test1LivroNPreco50() {  
        double expectedPrice = 50;
        Livro biblia = new Livro(OrigemLivro.NACIONAL);
        Livro[] livros = new Livro[1];
        livros[0] = biblia;
        double preco = Locadora.comprarLivros(livros);
        assertEquals(expectedPrice, preco, 0.001);
    }
    
    @Test
    public void test1LivroIPreco70() {  
        double expectedPrice = 70;
        Livro biblia = new Livro(OrigemLivro.INTERNACIONAL);
        Livro[] livros = new Livro[1];
        livros[0] = biblia;
        double preco = Locadora.comprarLivros(livros);
        assertEquals(expectedPrice, preco, 0.001);
    }
    
    @Test
    public void test2LivrosNPreco96() {  
        double expectedPrice = 96;
        Livro biblia = new Livro(OrigemLivro.NACIONAL);
        Livro alcorao = new Livro(OrigemLivro.NACIONAL);
        Livro[] livros = new Livro[2];
        livros[0] = biblia;
        livros[1] = alcorao;
        double preco = Locadora.comprarLivros(livros);
        assertEquals(expectedPrice, preco, 0.001);
    }
    
    @Test
    public void testVazioLivrosPreco0() {
        double expectedPrice = 0; 
        double preco = Locadora.comprarLivros(new Livro[0]);
        assertEquals(expectedPrice, preco, 0.001);
    }
    
    @Test
    public void test2LivrosINPreco1152() {  
        double expectedPrice = 120-0.04*120;
        Livro biblia = new Livro(OrigemLivro.INTERNACIONAL);
        Livro alcorao = new Livro(OrigemLivro.NACIONAL);
        Livro[] livros = new Livro[2];
        livros[0] = biblia;
        livros[1] = alcorao;
        double preco = Locadora.comprarLivros(livros);
        assertEquals(expectedPrice, preco, 0.001);
    }
    
}