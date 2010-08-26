require 'rubygems'
require 'spec'

describe Ranking do

  it 'should be an empty list when no country is given' do
    ranking = Ranking.new(nil)
    ranking.list.should == []
  end


end
