package AIPaladino;

public class PallyAI {

    public Battlefield bf;

    public PallyAI (Battlefield battlefield) {
        this.bf = battlefield;

    }

    public String action(){
        if(this.bf.pally.hp < 30){
            return "cura self";
        }else{
            if(this.bf.ally.hp < 30){
                return "cura ally";
            }
        }

        return "buff";
    }

}
