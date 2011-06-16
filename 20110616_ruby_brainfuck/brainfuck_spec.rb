require 'brainfuck'

describe 'Brainfuck' do
  it ',. com input [1] deve retornar 1' do
    brainfuck(',.', [1]).should == "1"
  end

  it ',. com input [2] deve retornar 2' do
    brainfuck(',.', [2]).should == "2"
  end
  
  it ',. com input [3] deve retornar 3' do
    brainfuck(',.', [3]).should == "3"
  end

  it ',+. com input [3] deve retornar 4' do
    brainfuck(',+.', [3]).should == "4"
  end
end
