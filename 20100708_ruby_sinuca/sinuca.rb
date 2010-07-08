class Jogada

  attr_accessor :pontos

  def initialize(bola_da_vez, bola_alvo, acertou, matou)
    if acertou
    @pontos = 0
    else
    @potos = -1
  end

end
