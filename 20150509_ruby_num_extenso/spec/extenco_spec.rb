require 'spec_helper'
require 'extenso'

describe 'Extenso' do
  it '0 retorna zero' do
    expect(0.extenso).to eq('zero')
  end
	it '1 retorna um' do
    expect(1.extenso).to eq('um')
  end
  it '2 retorna dois' do
    expect(2.extenso).to eq('dois') 
  end 
  it '3 retorna tres' do
    expect(3.extenso).to eq('três')
  end
  it '4 retorna quatro' do
    expect(4.extenso).to eq('quatro')
  end
  it '5 retorna cinco' do
    expect(5.extenso).to eq('cinco')
  end
  it '6 retorna seis' do
    expect(6.extenso).to eq('seis')
  end
  it '7 retorna sete' do
    expect(7.extenso).to eq('sete')
  end
  it '8 retorna oito' do
    expect(8.extenso).to eq('oito')
  end
  it '9 retorna nove' do
    expect(9.extenso).to eq('nove')
  end 
  it '10 retorna dez' do
    expect(10.extenso).to eq('dez')
  end
  it '11 retorna onze' do
    expect(11.extenso).to eq('onze')
  end
    it '12 retorna doze' do
    expect(12.extenso).to eq('doze')
  end
    it '13 retorna treze' do
    expect(13.extenso).to eq('treze')
  end
    it '14 retorna quatorze' do
    expect(14.extenso).to eq('quatorze')
  end
    it '15 retorna quinze' do
    expect(15.extenso).to eq('quinze')
  end  
    it '16 retorna dezesseis' do
    expect(16.extenso).to eq('dezesseis')
  end
    it '17 retorna dezessete' do
    expect(17.extenso).to eq('dezessete')
  end
    it '18 retorna dezoito' do
    expect(18.extenso).to eq('dezoito')
  end
    it '19 retorna dezenove' do
    expect(19.extenso).to eq('dezenove')
  end
  it '20 retorna vinte' do
    expect(20.extenso).to eq('vinte')
  end
  it '21 retorna vinte e um' do
    expect(21.extenso).to eq('vinte e um')
  end
  it '35 retorna trinta e cinco' do
    expect(35.extenso).to eq('trinta e cinco')
  end
  it '100 retorna cem' do
    expect(100.extenso).to eq('cem')
  end
  it '101 retorna cento e um' do
    expect(101.extenso).to eq('cento e um')
  end
end