require 'rubygems'
require 'spec'
require 'bolao'

describe 'bolao' do
  it '"Mario" nao acerta nada' do
    apostador1 = "Mario"
    bolao(apostador1, "0x0", "2x1").should == [apostador1, 0]
  end
  it '"Mario" acerta um resultado' do
    apostador1 = "Mario"
    bolao(apostador1, "0x1", "2x1").should == [apostador1, 1]
  end
end
