# Peças
P = :preto
B = :branco
X = 1

class Reversi
  attr_accessor :matriz
  def initialize
    @matriz = [
      [0,0,0,0],
      [0,P,B,0],
      [0,B,P,0],
      [0,0,0,0]
    ]
  end
  
  def marca_possivel(x, y)
    @matriz[x][y] = X
  end
end

def jogadas_possiveis(tabuleiro, jogador)
  if jogador == P
    tabuleiro.marca_possivel(0, 2)
    tabuleiro.marca_possivel(1, 3)
    tabuleiro.marca_possivel(2, 0)
    tabuleiro.marca_possivel(3, 1)
  else 
    tabuleiro.marca_possivel(0, 1) 
    tabuleiro.marca_possivel(1, 0)
    tabuleiro.marca_possivel(2, 3)
    tabuleiro.marca_possivel(3, 2)
  end
  
  return tabuleiro.matriz
end
