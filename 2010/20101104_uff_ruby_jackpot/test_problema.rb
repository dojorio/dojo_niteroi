require 'problema'

describe 'jackpot' do

  it 'should return 300 when sequence of 7 and bet 1' do
    game = [
      [X,B,X],
      [X,S,X],
      [S,S,S],
    ]
    jackpot(game, 1).should == 300
  end

  it 'should return 600 when sequence of 7 in line 3 and bet 2' do
    game = [
      [X,B,X],
      [X,S,X],
      [S,S,S],
    ]
    jackpot(game, 2).should == 600
  end

  it 'should return 3 when sequence of berry and bet 1' do
    game = [
      [X,B,X],
      [X,S,X],
      [B,B,B],
    ]
    jackpot(game, 1).should == 3
  end

  it 'should return 6 when sequence of berry and bet 2' do
    game = [
      [X,B,X],
      [X,S,X],
      [B,B,B],
    ]
    jackpot(game, 2).should == 6
  end

  it 'should return 300 when sequence of 7 in line 2 and bet 1' do
    game = [
      [X,B,X],
      [S,S,S],
      [B,X,X],
    ]
    jackpot(game, 1).should == 300
  end

  it 'should return 3 when sequence of berry in line 2 and bet 1' do
    game = [
      [X,B,X],
      [B,B,B],
      [X,S,X],
    ]
    jackpot(game, 1).should == 3
  end

  it 'should return 300 when sequence of seven in left to right diagonal and bet 1' do
    game = [
      [S,B,X],
      [S,S,B],
      [X,X,S],
    ]
    jackpot(game, 1).should == 300
  end

  it 'should return 300 when sequence of seven in right to left diagonal and bet 1' do
    game = [
      [X,B,S],
      [S,S,B],
      [S,X,X],
    ]
    jackpot(game, 1).should == 300
  end

end
