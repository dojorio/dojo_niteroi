require 'rubygems'
require 'spec'
require 'jokenpo.rb'

describe 'jokenpo' do

  it 'tesoura_contra_tesoura_retorna_empate' do
    jokenpo('tesoura', 'tesoura').should == 'empate'
  end

  it 'papel_contra_papel_retorna_empate' do
    jokenpo('papel', 'papel').should == 'empate'
  end

  it 'tesoura_contra_papel_retorna_tesoura' do
    jokenpo('tesoura', 'papel').should == 'tesoura'
  end

  it 'tesoura_contra_pedra_retorna_pedra' do
    jokenpo('tesoura', 'pedra').should == 'pedra'
  end

end
