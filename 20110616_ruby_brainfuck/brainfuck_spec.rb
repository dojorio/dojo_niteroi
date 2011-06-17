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

  it ',+. com input [5] deve retornar 6' do
    brainfuck(',+.', [5]).should == "6"
  end
  
  it ',++. com input [5] deve retornar 7' do
    brainfuck(',++.', [5]).should == "7"
  end

  it ',+++. com input [5] deve retornar 8' do
    brainfuck(',+++.', [5]).should == "8"
  end

  it ',-. com input [5] deve retornar 4' do
    brainfuck(',-.', [5]).should == "4"
  end
  
  it ',-++--++. com input [1] deve retornar 2' do
    brainfuck(',-++--++.', [1]).should == "2"  
  end
  
  it ',,. com input [1,2] deve retornar 2' do
    brainfuck(',,.', [1,2]).should == "2"
  end
  
  it ',,. com input [3,5] deve retornar 5' do
    brainfuck(',,.', [3,5]).should == "5"
  end
  
  it ',,,. com input [3,5,4] deve retornar 4' do
    brainfuck(',,,.', [3,5,4]).should == "4"
  end

  it ',+,. com input [10,12] deve retornar 4' do
    brainfuck(',+,.', [10,12]).should == "12"
  end

  it ',++,. com input [10,14] deve retornar 4' do
    brainfuck(',+,.', [10,14]).should == "14"
  end
end





















