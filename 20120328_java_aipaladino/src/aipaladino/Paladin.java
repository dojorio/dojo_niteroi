package aipaladino;

public class Paladin {

    private int hp;
    private boolean buffed = false;

    public Paladin(int hp) {
        this.hp = hp;
    }

    public String ai(Foe foe) {
        if (this.hp <= 20 && foe.getHp() != 1) {
            return this.cure();
        }
        if (!this.buffed) {
            return this.buff();
        }
        return this.pow(foe);

    }

    public String buff() {
        this.buffed = true;
        return "buff";
    }

    public String pow(Foe foe) {
        foe.takeDmg(15);
        return "pow";
    }

    public String cure() {
        this.hp += 40;
        return "cure";
    }

    public int getHp() {
        return this.hp;
    }

    public void setHp(int hp) {
        this.hp = hp;
    }
}
