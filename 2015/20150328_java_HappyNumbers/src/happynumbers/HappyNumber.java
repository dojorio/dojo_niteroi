package happynumbers;


public class HappyNumber {
    
    private int number;
    
    public HappyNumber(int number){
        this.number = number;
    }
    
    public boolean isHappy() {
        String textNumber = Integer.toString(number);
    
        int soma = 0;
        int posicao;

        for(int i = 0; i < textNumber.length() ; i++){
            posicao = (int) Math.pow(textNumber.charAt(i) - '0', 2);
            //charAt(x) retorna a posicão 'x' de uma sequencia de caracteres.
            //posição i=0 fica: 48 - 48 = 0
            //posição i=1 fica: 49 - 48 = 1
            soma += posicao;
        }

        if (soma == 10){
            return true;
        }
        
        if (soma > 1){
            return false;
        }
        return true;
               
    }
    
}
