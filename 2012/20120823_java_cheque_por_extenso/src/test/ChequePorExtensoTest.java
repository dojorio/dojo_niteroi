package test;

import static org.junit.Assert.assertEquals;

import org.junit.Test;

import code.ChequePorExtenso;

public class ChequePorExtensoTest {

	@Test
	public void passaUmERetornaUmCentavo() {
		ChequePorExtenso cheque = new ChequePorExtenso();
		assertEquals("um centavo", cheque.escrevePorExtenso(0.01));
	}
	
	@Test
	public void passaDezERetornaDezCentavos() {
		ChequePorExtenso cheque = new ChequePorExtenso();
		assertEquals("dez centavos", cheque.escrevePorExtenso(0.10));
	}
	
	@Test
	public void passaUmERetornaUmReal() {
		ChequePorExtenso cheque = new ChequePorExtenso();
		assertEquals("um real", cheque.escrevePorExtenso(1.00));
		
	}
	@Test
	public void passaCincoERetornaCincoCentavos() {
		ChequePorExtenso cheque = new ChequePorExtenso();
		assertEquals("cinco centavos", cheque.escrevePorExtenso(0.05));
	}
	
	@Test
	public void passaCinquentaERetornaCinquentaCentavos() {
		ChequePorExtenso cheque = new ChequePorExtenso();
		assertEquals("cinquenta centavos", cheque.escrevePorExtenso(0.50));
	}
	@Test
	public void passaVinteECincoERetornaVinteECincoCentavos(){
		ChequePorExtenso cheque = new ChequePorExtenso();
		assertEquals("vinte e cinco centavos",cheque.escrevePorExtenso(0.25));
	}
	
}
