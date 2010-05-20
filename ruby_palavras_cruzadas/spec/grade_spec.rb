require File.dirname(__FILE__) + '/spec_helper'

describe Grade do

  ESPERADO = <<GRADE
###########
#    #    #
#    #    #
###########
GRADE
    
  it "deve retornar dois quadrados vazios juntos na mesma linha quando houver dois underlines" do
    Grade.new('__').draw.should == ESPERADO
  end
  
end

