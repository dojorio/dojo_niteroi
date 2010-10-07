require 'rubygems'
require 'spec'
require 'assassino.rb'

describe 'Assassino' do

  before(:each) do
    0.morto = false
    1.morto = false
    2.morto = false
    3.morto = false
  end

  it 'grupo de 1 com passo 1 deve morrer [0]' do
    pessoas = 1
    passo = 1
    assassina(pessoas, passo).should == [0]
  end

  it 'grupo de 2 com passo 1 deve morrer [0, 1]' do
    pessoas = 2
    passo = 1
    assassina(pessoas, passo).should == [0, 1]
  end

  it 'grupo de 3 com passo 1 deve morrer [0, 1, 2]' do
    pessoas = 3
    passo = 1
    assassina(pessoas, passo).should == [0, 1, 2]
  end

  it 'grupo de 1 com passo 2 deve morrer [0]' do
    pessoas = 1
    passo = 2
    assassina(pessoas, passo).should == [0]
  end

  it 'grupo de 2 com passo 2 deve morrer [1, 0]' do
    pessoas = 2
    passo = 2
    assassina(pessoas, passo).should == [1, 0]
  end

  it 'grupo de 2 com passo 3 deve morrer [0, 1]' do
    pessoas = 2
    passo = 3
    assassina(pessoas, passo).should == [0, 1]
  end

  it 'grupo de 2 com passo 4 deve morrer [1, 0]' do
    pessoas = 2
    passo = 4
    assassina(pessoas, passo).should == [1, 0]
  end

  it 'grupo de 3 com passo 2 deve morrer [1,0,2]' do
    pessoas = 3
    passo = 2
    assassina(pessoas, passo).should == [1, 0, 2]
  end

end
