require 'rubygems'
require 'spec'
require 'ascii_grid'

describe "Conversor" do

  it 'should return an empty string when list is empty' do
    conversor([]).should == ""
  end

  it "should be 'A' when input is [65, 0, 0]" do
    conversor([65, 0, 0]).should == "A"
  end

  it "should be 'B' when input is [66, 0, 0]" do
    conversor([66, 0, 0]).should == "B"

end
