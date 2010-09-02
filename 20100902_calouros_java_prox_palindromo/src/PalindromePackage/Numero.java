package PalindromePackage;

import java.util.ArrayList;

public class Numero {

    private int value;

    public Numero() {
    }

    public Numero(int value) {
        this.value = value;
    }

    public int nextPalidrome() {

        do{
            ++value;
        }
        while(!isPalindrome());
        return value;


    }

    public boolean isPalindrome()
    {
        String strNumero = value+"";
        for(int i = 0; i < strNumero.length()/2; i++){
            ArrayList hey = new ArrayList();
            if(strNumero.charAt(i) != strNumero.charAt(strNumero.length()-i-1))
                return false;
        }
        return true;
    }
}
