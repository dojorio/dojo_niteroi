package piratas;

/**
 *
 * @author rodrigo
 */
public class Piratas {

    public int getValorMoeda(int indice) {
        switch (indice) {
            case 0:
                return 1;
            case 1:
                return 2;
            case 2:
                return 5;
            case 3:
                return 10;
            default:
                return 0;
        }
    }

    public int distribuir(int[] moedas, int numeroPiratas) {
        int total = 0;
        for (int i = 0; i < moedas.length; i++) {
            total += moedas[i] * getValorMoeda(i);
        }

        int valordesejado = total / numeroPiratas;
        int valorobtido = 0;

        for (int i = 3; i >= 0; i--) {
            while (valorobtido <= valordesejado) {
                if (moedas[i] >= 1 && valorobtido + getValorMoeda(i) <= valordesejado) {
                    valorobtido += getValorMoeda(i);
                    moedas[i] -= 1;
                }
                else {
                    break;
                }
            }
        }
        if (valorobtido == valordesejado) {
            return valordesejado;
        }
        return -1;
    }
}
