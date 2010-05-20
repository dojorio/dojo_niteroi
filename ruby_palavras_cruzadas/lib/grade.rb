class Grade
  
  QUADRADO_PREENCHIDO = <<QUADRADO
######
######
######
######
QUADRADO

  
  def initialize(entrada)
    @entrada = entrada
  end
  
  def draw
    QuadradoVazio.com_todas_bordas+QuadradoVazio.new("_").draw    
  end
  
end