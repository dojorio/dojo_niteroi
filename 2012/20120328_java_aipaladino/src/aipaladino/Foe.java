package aipaladino;

public class Foe {
    
    private int hp;
    
    public Foe(int hp) {
        this.hp = hp;
    }

    public int getHp(){
    return this.hp;
    }
    
    public void setHp(int hp) {
        this.hp = hp;
    }
    
    public void takeDmg(int dmg) {
        this.hp -= dmg;
        this.hp = this.hp < 0 ? 0 : this.hp;
    }
}
