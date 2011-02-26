require "jokenpo"

describe "jokenpo" do

  it "deve retornar empate quando for papel x papel" do
    resultado("papel", "papel").should == "empate"
  end
  
  it "deve retornar tesoura quando for tesoura x papel" do
    resultado("tesoura", "papel").should == "tesoura"
  end

  it "deve retornar pedra quando for tesoura x pedra" do
    resultado("tesoura", "pedra").should == "pedra"
  end
  
  it "deve retornar papel quando for pedra x papel" do
    resultado("pedra", "papel").should == "papel"
  end
  
  it "deve retornar pedra quando for pedra x tesoura" do
    resultado("pedra", "tesoura").should == "pedra"
  end
  
  it "deve retornar papel quando for papel x pedra" do
    resultado("papel", "pedra").should == "papel"
  end
  
  it 'deve retornar mensagem invalida quando a entrada é invalida' do 
    resultado('ok3','ok4').should == 'Não da certo'
  end
 
  
end
