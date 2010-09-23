require 'rubygems'
require 'spec'
require 'pau_no_gato'

describe Gato do

  it 'nao morre quando atiram o pau nele' do
    gato = Gato.new()
    gato.atacado('pau')
    gato.morto.should == false
  end

  it 'morre quando atiram a geladeira nele' do
    gato = Gato.new()
    gato.atacado('geladeira')
    gato.morto.should == true
  end

  it 'morre quando atiram a geladeira e um pau nele' do
    gato = Gato.new()
    gato.atacado('geladeira')
    gato.atacado('pau')
    gato.morto.should == true
  end

  it 'berra quando atiram o pau nele' do
    gato = Gato.new()
    gato.atacado('pau')
    gato.berrando.should == true
  end

  it 'novo esta vivo e nao esta berrando' do
    gato = Gato.new()
    gato.berrando.should == false
    gato.morto.should == false
  end

  it 'nao berra quando tacam a geladeira' do
    gato = Gato.new()
    gato.atacado('geladeira')
    gato.berrando.should == false
  end

  it 'nao berra quando tacam geladeira e pau' do
    gato = Gato.new()
    gato.atacado('geladeira')
    gato.atacado('pau')
    gato.berrando.should == false
  end

  it 'nao berra quando tacam pau e geladeira' do
    gato = Gato.new()
    gato.atacado('pau')
    gato.atacado('geladeira')
    gato.berrando.should == false
  end
end

describe DonaChica do
  it 'se admira quando o gato berra' do
    gato = Gato.new()
    gato.atacado('pau')
    dona_chica = DonaChica.new()
    dona_chica.admira_se(gato)
    dona_chica.admirada.should == true
  end

  it 'nao se admira quando o gato nao berra' do
    gato = Gato.new()
    dona_chica = DonaChica.new()
    dona_chica.admira_se(gato)
    dona_chica.admirada.should == false
  end

  it 'se admira quando gato berra e continua admirada quando gato morre' do
    gato = Gato.new()
    dona_chica = DonaChica.new()
    gato.atacado('pau')
    dona_chica.admira_se(gato)
    gato.atacado('geladeira')
    dona_chica.admira_se(gato)
    dona_chica.admirada.should == true
  end

end
