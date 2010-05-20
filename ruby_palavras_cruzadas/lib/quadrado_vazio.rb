class QuadradoVazio
  
  COM_TODAS_BORDAS = <<QUADRADO
######
#    #
#    #
######
QUADRADO

  SEM_BORDA_ESQUERDA = <<QUADRADO
#####
    #
    #
#####
QUADRADO

  SEM_BORDA_SUPERIOR = <<QUADRADO
#    #
#    #
######
QUADRADO
  
  SEM_BORDA_SUPERIOR_E_ESQUERDA = <<QUADRADO
    #
    #
#####
QUADRADO
  attr_accessor :quadrado
  def initialize(quadrado)
    @quadrado = qudrado
  end
  
  def self.com_todas_bordas
    QuadradoVazio.new(COM_TODAS_BORDAS)
  end
  
  def self.sem_borda_esquerda
    SEM_BORDA_ESQUERDA
  end
  
  def self.sem_borda_superior
    SEM_BORDA_SUPERIOR
  end
  
  def self.sem_borda_superior_e_esquerda
    SEM_BORDA_SUPERIOR_E_ESQUERDA
  end
  
  def +(outro)
    self.quadrado + outro.quadrado
  end
  
end