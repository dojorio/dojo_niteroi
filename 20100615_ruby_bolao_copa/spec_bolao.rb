require 'rubygems'
require 'spec'
require 'bolao'

describe 'soma' do
  it 'test pass' do
    soma(1, 1).should == 2
  end
end
