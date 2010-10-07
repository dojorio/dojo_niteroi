
import java.util.HashMap;

public class NumeroRomano {

    private String numero;
    private HashMap tabelaRomanos = new HashMap();

    public NumeroRomano(String numero) {
        this.numero = numero;
        this.tabelaRomanos.put('I', 1);
        this.tabelaRomanos.put('V', 5);
    }

    public int paraInteiro() {
        int valor = 0;

        for (int i = 0; i < this.numero.length(); i++) {
            valor += (Integer) tabelaRomanos.get(numero.charAt(i));
        }

        return valor;
    }

}
