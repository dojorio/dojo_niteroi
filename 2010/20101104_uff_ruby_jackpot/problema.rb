S = 'seven'
J = 'joker'
B = 'berry'
C = 'coins'
W = 'witch'
X = 'x'

VALUES = {
  S => 300, 
  B => 3
}

def jackpot(game, bet)
  if [game[0][0],game[0][0],game[0][0]] == [game[0][0],game[1][1],game[2][2]]
     return VALUES[game[1][1]]*bet   
  end

  if [game[0][2],game[0][2],game[0][2]] == [game[0][2],game[1][1],game[2][0]]
    return VALUES[game[1][1]]*bet   
  end

  for line in game
    if [line[0], line[0], line[0]] == line
      return VALUES[line[0]]*bet
    
    end
    
  end



 
  
end
