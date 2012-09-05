package code;

import java.util.HashMap;

public class ChequePorExtenso {
	class Extenso {
		HashMap<Integer, String> numeros = new HashMap<Integer, String>();
		int numero;
		
		public Extenso(int numero) {
			numeros.put(1, "um");
			numeros.put(5, "cinco");
			numeros.put(10, "dez");
			numeros.put(20, "vinte");
			numeros.put(50, "cinquenta");
			
			this.numero = numero;
		}
		
		public String toString(){
			return numeros.get(numero);
		}
	}
	
	public String escrevePorExtenso(double numero) {
		String resultado = "";
		if (numero == 0.01) {
			return "um centavo";
		} else if (numero < 1.0) {
			int centavos = (int) (numero * 100);
			int unidade = centavos % 10;
			int dezena = centavos - unidade;
			if(dezena <= 0){
				resultado += new Extenso(unidade);
			} else if(unidade>0){
				resultado += new Extenso(dezena) + " e " + new Extenso(unidade);
			} else{
				resultado += new Extenso(dezena);
			}
			return resultado + " centavos";
		} else {
			return "um real";
		}

	}
}