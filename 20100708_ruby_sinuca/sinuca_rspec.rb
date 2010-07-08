# Exemplo rspec ruby
# "spec banheiro_spec.rb" to run on Terminal


require 'rubygems'
require 'spec'
require 'sinuca'

describe Jogada do
  it 'acerta a bola da vez e nao mata deve retornar 0' do
    bola_da_vez = 1
    bola_alvo = bola_da_vez
    acertou = true
    matou = false
    Jogada.new(bola_da_vez, bola_alvo, acertou, matou).pontos.should == 0
