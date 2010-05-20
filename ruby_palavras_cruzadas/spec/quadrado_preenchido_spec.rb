require File.dirname(__FILE__) + '/spec_helper'

describe QuadradoPreenchido do

  ESPERADO = <<QUADRADO
######
######
######
######
QUADRADO
    
  it "deve retornar um único quadrado preenchido quando houver um único X" do
    QuadradoPreenchido.new('X').draw.should == ESPERADO
  end
  
end
