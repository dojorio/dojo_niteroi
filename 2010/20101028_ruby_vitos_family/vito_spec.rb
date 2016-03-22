require 'rubygems'
require 'spec'
require 'vito'

describe CampoMinado do

  it 'deve ser 2x2 sem bomba' do
    campo = CampoMinado.new([
        ['-', '-'],
        ['-', '-']
    ])
    campo.resultado.should == [
        [0, 0],
        [0, 0]
    ]
  end

  it 'deve ser 3x3 sem bomba' do
    campo = CampoMinado.new([
        ['-', '-', '-'],
        ['-', '-', '-'],
        ['-', '-', '-'],
    ])
    campo.resultado.should == [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]
  end

  it 'deve ser 4x4 sem bomba' do
    campo = CampoMinado.new([
        ['-', '-', '-', '-'],
        ['-', '-', '-', '-'],
        ['-', '-', '-', '-'],
        ['-', '-', '-', '-'],
    ])
    campo.resultado.should == [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]
  end

  it 'deve ser 2x2 com bomba em [(0,0)]' do
    campo = CampoMinado.new([
        ['*', '-'],
        ['-', '-'],
    ])
    campo.resultado.should == [
        ['*', 1],
        [ 1,  1]
    ]
  end

  it 'deve ser 2x2 com bomba em [(0,1)]' do
    campo = CampoMinado.new([
        ['-', '*'],
        ['-', '-'],
    ])
    campo.resultado.should == [
        [ 1, '*'],
        [ 1,  1 ]
    ]
  end








end
