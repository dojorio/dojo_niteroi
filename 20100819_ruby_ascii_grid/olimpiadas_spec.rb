require 'rubygems'
require 'spec'
require 'olimpiadas'

describe Problema do
  it 'test pass' do
    Problema.new.soma(1, 1).should == 2
  end
  it 'test not pass' do
    Problema.new.soma(1, 2).should == 2
  end
end
