$LOAD_PATH << './'
require 'happy_numbers'

describe 'HappyNumbers' do

  it 'numero 1 deve ser feliz' do
    is_happy_number?(1).should be_true
    
  end
  
  it 'numero 2 deve ser infeliz' do
    is_happy_number?(2).should be_false
  end
  
  it 'numero 3 deve ser infeliz' do
    is_happy_number?(3).should be_false
  end
  
  it 'numero 4 deve ser infeliz' do
  is_happy_number?(4).should be_false  
  end
  
  it 'numero 5 deve ser infeliz' do
    is_happy_number?(5).should be_false  
  end
  
  it 'numero 6 deve ser infeliz' do
    is_happy_number?(6).should be_false  
  end
  
  it 'numero 8 deve ser infeliz' do
    is_happy_number?(8).should be_false
  end 
  
  it 'numero 7 deve ser feliz' do
    is_happy_number?(7).should be_true
  end
  
  it 'numero 37 deve ser infeliz' do
    is_happy_number?(37).should be_false
  end 
    
  
end
