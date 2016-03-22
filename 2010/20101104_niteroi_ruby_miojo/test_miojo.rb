require 'miojo'

describe 'miojo' do
  
  it 'should receive hourglass 2 and 3 and miojo 1 and return 3' do
    miojo(2,3,1).should == 3
  end
  
  it 'should receive hourglass 3 and 4 and miojo 1 and return 4' do
    miojo(3,4,1).should == 4
  end
  
  it 'should receive hourglass 3 and 5 and miojo 2 and return 5' do
    miojo(3,5,2).should == 5
  end
  
  it 'should receive hourglass 3 and 4 and miojo 2 and return 6' do
    miojo(3,4,2).should == 6
  end
  
  it 'should receive hourglass 5 and 7 and miojo 3 and return 10' do
    miojo(5,7,3).should == 10
  end
  
  it 'should receive hourglass 4 and 9 and miojo 3 and return 12' do
    miojo(4,9,3).should == 12
  end
  
  it 'should receive hourglass 4 and 9 and miojo 2 and return 18' do
    miojo(4,9,2).should == 18
  end
  
  it 'should receive hourglass 15 and 22 and miojo 14 and return 44' do
    miojo(15,22,14).should == 44
  end
  
  
  
  
  
  
  
  
end


