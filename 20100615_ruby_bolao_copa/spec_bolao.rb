require 'rubygems'
require 'spec'
require 'bolao'

describe 'bolao' do
  it 'apostador 1 nao acerta nada' do
    bolao(apostador1, "0x0", "2x1").should == [apostador1, 0]
  end
end
