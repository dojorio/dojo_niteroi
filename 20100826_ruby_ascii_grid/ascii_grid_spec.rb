require 'rubygems'
require 'spec'
require 'ascii_grid'

describe "Conversor" do

  it 'should return an empty string when list is empty' do
    conversor([]) == ""
  end

end
