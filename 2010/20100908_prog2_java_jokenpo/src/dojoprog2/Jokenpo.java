/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

package dojoprog2;

/**
 *
 * @author casa
 */
import java.util.HashMap;

public class Jokenpo {
    HashMap dicJokenpo;
    public Jokenpo(){
        dicJokenpo = new HashMap();
        HashMap pedra = new HashMap();
        pedra.put("pedra", "empate");
        pedra.put("tesoura", "pedra");
        pedra.put("papel", "papel");
        
        HashMap papel = new HashMap();
        papel.put("papel", "empate");
        papel.put("tesoura", "tesoura");
        papel.put("pedra", "papel");
        
        HashMap tesoura = new HashMap();
        tesoura.put("tesoura", "empate");
        tesoura.put("pedra", "pedra");
        tesoura.put("papel", "tesoura");
        
        dicJokenpo.put("pedra", pedra);
        dicJokenpo.put("papel", papel);
        dicJokenpo.put("tesoura", tesoura);
    }


    public String jogar(String jogada1, String jogada2){
        return (String)((HashMap) (dicJokenpo.get(jogada1))).get(jogada2);
    }
}
