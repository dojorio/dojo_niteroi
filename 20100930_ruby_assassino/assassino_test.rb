require 'rubygems'
require 'spec'
require 'assassino.rb'

describe 'Assassino' do

  it 'morre 1 com passo 1' do
    assassina(1, 1).should == [0]
  end

end
