
package dojo;

import java.util.HashMap;

public class Romano {

    HashMap<Integer, String> map;

    public Romano() {
        map = new HashMap();
        map.put(1,"I");
        map.put(2,"II");
        map.put(3, "III");
        map.put(4, "IV");
        map.put(5, "V");
        map.put(9, "IX");
        map.put(10, "X");
        map.put(40, "XL");
    }

    public String repete(int count) {
        String result = "";
        for (int i = 0; i < count; i++) {
            result += map.get(10);
        }
        return result;
    }


    public String converteDeInteiro(int numeroInteiro) {
        if (numeroInteiro < 1) {
            return "";
        }

        if (numeroInteiro > 40){
            return map.get(40) + converteDeInteiro(numeroInteiro % 40);
        }

        if (numeroInteiro > 10 && numeroInteiro < 40) {
            int multiplicador = numeroInteiro / 10;
            return repete(multiplicador) + converteDeInteiro(numeroInteiro % 10);
        }

        if (numeroInteiro > 5 && numeroInteiro < 9) {
            return map.get(5) + map.get(numeroInteiro % 5);
        }

        return map.get(numeroInteiro);

    }

}
