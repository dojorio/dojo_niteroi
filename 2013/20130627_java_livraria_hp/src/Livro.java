/**
 *
 * @author rodcastro
 */

public class Livro {

    public OrigemLivro tipo;
    public int qualificativo;
    public static final int LANCAMENTO = 1;
    public static final int CAPA_DURA = 2;
    public static final int OUTRO_IDIOMA = 3;
    public static final int SEMI_NOVO = 4;

    public Livro() {
        tipo = OrigemLivro.NACIONAL;
        qualificativo = 0;
    }

    public Livro(OrigemLivro tipo) {
        this.tipo = tipo;

    }

    public double getPreco() {
        double preco = 0;
        if (tipo == OrigemLivro.NACIONAL) {
            preco += 50;
        } else {
            preco += 70;
        }
        return preco + calculaAdicional();
    }
    
    private double calculaAdicional() {
        double adicional = 0;
        switch (qualificativo) {
            case LANCAMENTO:
                adicional = 14.99;
                break;
            case CAPA_DURA:
                adicional = 9.99;
                break;
            case OUTRO_IDIOMA:
                adicional = 4.99;
                break;
            case SEMI_NOVO:
                adicional = 7.49;
                break;
        }
        return adicional;
    }
}