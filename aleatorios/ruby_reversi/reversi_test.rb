require 'rubygems'
require 'spec'
require './reversi.rb'

describe 'Reversi' do
  
  before(:each) do
    @tabuleiro = Reversi.new
  end
  
  it 'posicoes do branco jogar no tabuleiro inicial' do
    possibilidades = [
      [0,X,0,0],
      [X,P,B,0],
      [0,B,P,X],
      [0,0,X,0]
      ]
    
    jogadas_possiveis(@tabuleiro, B).should == possibilidades
  end
  
  it 'posicoes do preto jogar no tabuleiro inicial' do
    possibilidades = [
      [0,0,X,0],
      [0,P,B,X],
      [X,B,P,0],
      [0,X,0,0]
      ]
    
    jogadas_possiveis(@tabuleiro, P).should == possibilidades

  end  it 'possibilidades do branco na segunda rodada' do
      @tabuleiro[0][2] = P
      @tabuleiro[1][2] = P
    
      possibilidades = [
        [0,X,P,X],
        [0,P,P,0],
        [0,B,P,X],
        [0,0,0,0]
        ]

      jogadas_possiveis(@tabuleiro, P).should == possibilidades
    end
end