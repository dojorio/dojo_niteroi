require File.dirname(__FILE__) + '/spec_helper'

describe QuadradoVazio do

  COM_TODAS_BORDAS1 = <<QUADRADO
######
#    #
#    #
######
QUADRADO
    
  SEM_BORDA_ESQUERDA1 = <<QUADRADO1
#####
    #
    #
#####
QUADRADO1

  SEM_BORDA_SUPERIOR1 = <<QUADRADO
#    #
#    #
######
QUADRADO
    
  SEM_BORDA_SUPERIOR_E_ESQUERDA1 = <<QUADRADO
    #
    #
#####
QUADRADO

DOIS_PRIMEIROS_QUADRADOS1 = <<QUADRADO
###########
#    #    #
#    #    #
###########
QUADRADO
    
  it "deve retornar um único quadrado vazio quando houver um único underline" do
    QuadradoVazio.com_todas_bordas.should == COM_TODAS_BORDAS1
  end
  
  it "deve retornar um quadrado sem a borda esquerda" do
    QuadradoVazio.sem_borda_esquerda.should == SEM_BORDA_ESQUERDA1
  end
  
  it "deve retornar um quadrado sem a borda superior" do
    QuadradoVazio.sem_borda_superior.should == SEM_BORDA_SUPERIOR1
  end
  
  it "deve retornar um quadrado sem a borda superior e esquerda" do
    QuadradoVazio.sem_borda_superior_e_esquerda.should == SEM_BORDA_SUPERIOR_E_ESQUERDA1
  end
  
  it "deve retornar um quadrado somado ao outro" do
    (QuadradoVazio.com_todas_bordas+QuadradoVazio.sem_borda_esquerda).should == DOIS_PRIMEIROS_QUADRADOS1
  end
  
  
end
