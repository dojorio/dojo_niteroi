require 'intersecao'

describe 'intersecao' do
  
  it 'não deve retornar interseção para [0, 0], [1, 1] e [2, 2], [3, 3]' do
    retangulo_1 = Retangulo.new([0, 0], [1, 1])
    retangulo_2 = Retangulo.new([2, 2], [3, 3])
    
    intersecao = retangulo_1.intersecao(retangulo_2)
    intersecao.should == "Não possui interseção"
  end

  it "deve retornar [1, 1], [2, 2] para [0, 0], [2, 2] e [1, 1], [3, 3]" do
    retangulo_1 = Retangulo.new([0, 0], [2, 2])
    retangulo_2 = Retangulo.new([1, 1], [3, 3])
    
    intersecao = retangulo_1.intersecao(retangulo_2)
    intersecao.should == Retangulo.new([1, 1], [2, 2])
  end
  
  it "deve retornar [2, 2], [3, 3] para [1, 1], [3, 3] e [2, 2], [4, 4]" do
    retangulo_1 = Retangulo.new([1, 1], [3, 3])
    retangulo_2 = Retangulo.new([2, 2], [4, 4])
    
    intersecao = retangulo_1.intersecao(retangulo_2)
    intersecao.should == Retangulo.new([2, 2], [3, 3])
  end
      
  it 'não deve retornar interseção para [0, 0], [1, 2] e [4, 4], [6, 5]' do
    retangulo_1 = Retangulo.new([0, 0], [1, 2])
    retangulo_2 = Retangulo.new([2, 2], [3, 3])
    
    intersecao = retangulo_1.intersecao(retangulo_2)
    intersecao.should == "Não possui interseção"
  end
  
  it 'não deve retornar interseção para [4, 4], [6, 5] e [0, 0], [1, 2]' do
    retangulo_1 = Retangulo.new([2, 2], [3, 3])
    retangulo_2 = Retangulo.new([0, 0], [1, 2])
    
    intersecao = retangulo_1.intersecao(retangulo_2)
    intersecao.should == "Não possui interseção"
  end
  
  it 'não deve retornar interseção para [0, 0], [1, 1] e [0, 2], [1, 3]' do
    retangulo_1 = Retangulo.new([0, 0], [1, 1])
    retangulo_2 = Retangulo.new([0, 2], [1, 3])
    
    intersecao = retangulo_1.intersecao(retangulo_2)
    intersecao.should == "Não possui interseção"
  end
  
  it 'não deve retornar interseção para [0, 0], [2, 3] e [0, 2], [2, 4]' do
    retangulo_1 = Retangulo.new([0, 0], [2, 3])
    retangulo_2 = Retangulo.new([0, 2], [2, 4])
    
    intersecao = retangulo_1.intersecao(retangulo_2)
    intersecao.should == Retangulo.new([0, 2], [2, 3])
  end

  it 'não deve retornar interseção para [0, 2], [2, 4] e [0, 0], [2, 3]' do
    retangulo_1 = Retangulo.new([0, 2], [2, 4])
    retangulo_2 = Retangulo.new([0, 0], [2, 3])
    
    intersecao = retangulo_1.intersecao(retangulo_2)
    intersecao.should == Retangulo.new([0, 2], [2, 3])
  end

end
