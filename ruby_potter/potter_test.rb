require 'rubygems'
require 'spec'
require 'potter.rb'

describe 'alvaro viado' do
  it 'compra livro 5 sem desconto' do
    retorna_valor_pacote([0, 0, 0, 0, 1]).should == 8
  end  
  
  it 'compra livro 3 sem desconto' do
    retorna_valor_pacote([0, 0, 1, 0, 0]).should == 8
  end
  
  it 'compra 2 livros diferentes com 5% de desconto' do
    retorna_valor_pacote([1, 1, 0, 0, 0]).should == 15.2
  end
  
  it 'compra 3 livros diferentes com 10% de desconto' do
    retorna_valor_pacote([1, 1, 0, 1, 0]).should == 21.6
  end
  
  it 'compra 4 livros diferentes com 20% de desconto' do
    retorna_valor_pacote([1, 1, 0, 1, 1]).should == 25.6
  end

  it 'compra 5 livros diferentes com 25% de desconto' do
    retorna_valor_pacote([1, 1, 1, 1, 1]).should == 30
  end
  
  it 'compra 2 livros 5 sem desconto' do
    retorna_valor_pacote([0, 0, 0, 0, 2]).should == 16
  end
  
  #it 'compra 2 livros 5 e 1 livro 1 com 5% em 2 e 0% no outro' do
  #  retorna_valor_pacote([1, 0, 0, 0, 2]).should == 23.2
  # end
end

describe 'Operacoes de pacote' do
  it 'lista [ 1, 1, 1, 1, 2] gera pacote [0, 0, 0, 0, 1]' do
    gera_pacote([ 1, 1, 1, 1, 2]).should == [0, 0, 0, 0, 1]
  end
  
  it 'verifica se [0, 0, 0, 1, 0] o pacote eh final' do
    verifica_pacote_final([0, 0, 0, 1, 0]).should == true
  end
  
  it 'verifica se [0, 0, 0, 10, 0] o pacote eh final' do
    verifica_pacote_final([0, 0, 0, 10, 0]).should == true
  end
  
  it 'verifica se [1, 0, 0, 10, 0] o pacote eh final' do
    verifica_pacote_final([1, 0, 0, 10, 0]).should == false
  end
  
  it 'verifica se [10, 0, 0, 1, 0] o pacote eh final' do
    verifica_pacote_final([10, 0, 0, 1, 0]).should == false
  end  
end
