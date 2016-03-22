require 'rubygems'
require 'spec'
require 'ranking'
require 'country'

describe Ranking do

  it 'should be an empty list when no country is given' do
    ranking = Ranking.new(nil)
    ranking.list.should == []
  end

  it 'should be Brazil when only this country is given' do
    ranking = Ranking.new([Country.new("Brazil", 1, 2, 3)])
    ranking.list.should == ["Brazil"]
  end

  it 'should be Argentina when only this country is given' do
    ranking = Ranking.new([Country.new("Argentina", 0, 2, 4)])
    ranking.list.should == ["Argentina"]
  end

  it 'should be [Brazil, Argentina] when Brazil has more golden medals than Argentina' do
    brazil = Country.new("Brazil",2,0,0)
    argentina = Country.new("Argentina",1,0,0)
    ranking = Ranking.new([brazil, argentina])
    ranking.list.should == ["Brazil","Argentina"]
  end


end
