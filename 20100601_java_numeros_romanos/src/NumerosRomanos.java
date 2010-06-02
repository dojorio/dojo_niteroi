import java.util.HashMap;


public class NumerosRomanos {
	
	private HashMap hashMap;	
	
	public NumerosRomanos()
	{
		this.hashMap = new HashMap();
		this.hashMap.put(1, "I");
		this.hashMap.put(2, "II");
		this.hashMap.put(3, "III");
		this.hashMap.put(4, "IV");
		this.hashMap.put(5, "V");
		
	}

	public String paraInteiro(int numeroInteiro){
		if (numeroInteiro > 5) {
			int resto = numeroInteiro % 5;
			if(resto != 0){
				return (String)this.hashMap.get(5) + (String)this.hashMap.get(resto);
			}
		}
		
		
		return (String)this.hashMap.get(numeroInteiro);

	}
	
}
