# Exemplo rspec ruby
# "spec banheiro_spec.rb" to run on Terminal


require 'rubygems'
require 'spec'
require 'sinuca'

describe Problema do
  it 'test pass' do
    Problema.new.soma(1, 1).should == 2
  end
end
