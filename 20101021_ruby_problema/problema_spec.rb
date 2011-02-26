require 'problema'

describe 'fatora' do
    it 'should return [1] when we pass 1 to fatora' do
        fatora(1).should == [1]
    end

    it 'should return [2, 1] when we pass 2 to fatora' do
        fatora(2).should == [2, 1]
    end
    
    it 'should return [3, 1] when we pass 3 to fatora' do
        fatora(3).should == [3, 1]
    end

    it 'should return [2, 2, 1] when we pass 4 to fatora' do
        fatora(4).should == [2, 2, 1]
    end

    it 'should return [2, 3, 1] when we pass 6 to fatora' do
        fatora(6).should == [2, 3, 1]
    end

    it 'should return [5, 1] when we pass 5 to fatora' do
        fatora(5).should == [5, 1]
    end

    it 'should return [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1] when we pass 1024 to fatora' do
        fatora(1024).should == [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1]
    end

    it 'should return [3, 11, 31, 1] when we pass 1023 to fatora' do
        fatora(1023).should == [3, 11, 31, 1]
    end
end