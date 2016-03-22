
import java.util.HashMap;

/**
 *
 * @author rodcastro
 */
public class Locadora {

    public static final HashMap<Integer, Double> descontos = new HashMap<Integer, Double>();

    static {
        descontos.put(2, 0.96);
        descontos.put(3, 0.90);
        descontos.put(5, 0.80);
    }

    public static double comprarLivros(Livro[] livros) {
        double preco = 0;
        if (livros != null) {
            for (int i = 0; i < livros.length; i++) {
                Livro livro = livros[i];
                preco += livro.getPreco();
            }
            Double desconto = descontos.get(livros.length);
            if (desconto != null) {
                preco *= desconto;
            } else if (livros.length > 5) {
                preco *= 0.80;
            }
            return preco;
        }
        return 0;
    }
}