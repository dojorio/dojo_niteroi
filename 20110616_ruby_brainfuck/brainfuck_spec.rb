require 'brainfuck'

describe 'Brainfuck' do
  it ',. com input [1] deve retornar 1' do
    brainfuck(',.', [1]).should == 1
  end
end
