require "troco"

describe 'troco' do
  describe 'Troco' do
    it 'preco R$ 1,00, pagando R$ 2,00 deve retornar R$ 1,00' do
      calcula_troco(1, 2).should == {"R$ 1,00" => 1}
    end

    it 'preco R$ 1,00, pagando R$ 1,00 nao retorna troco' do
      calcula_troco(1, 1).should == {}
    end

    it 'preco R$ 1,00, pagando R$ 5,00 deve retornar R$ 4,00' do
      calcula_troco(1, 5).should == {"R$ 2,00" => 2}
    end

    it 'preco R$ 2,00, pagando R$ 7,00 deve retornar R$ 5,00' do
      calcula_troco(2, 7).should == {"R$ 5,00" => 1}
    end

    it 'preco R$ 3,00, pagando R$\ 5,00 deve retornar R$ 2,00' do
      calcula_troco(3, 5).should == {"R$ 2,00" => 1}
    end
  end

  describe 'Troco Otimizado' do

    describe "Casos simples em que o troco é uma nota" do
        notas = [1, 2, 5, 10, 20, 50, 100]
        notas.each do |nota|
            it "Troco #{nota} deve retornar R$ #{nota},00" do
                troco_otimizado(nota).should == { "R$ #{nota},00" => 1}
            end 
        end
    end

    it 'Troco 0 nao retorna troco' do
      troco_otimizado(0).should == {}
    end

    it 'Troco 4, retorna 2 de R$ 2,00' do
      troco_otimizado(4).should == {"R$ 2,00" => 2}
    end
  

    it 'Troco 40 retorna 2 de R$ 20,00' do
      troco_otimizado(40).should == {"R$ 20,00" => 2}
    end

    end

end
