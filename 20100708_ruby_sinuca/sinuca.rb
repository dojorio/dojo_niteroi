class Jogada

  attr_accessor :pontos

  def initialize(bola_da_vez, bola_alvo, acertou, matou)
    if acertou
      @pontos = 0
    else
      @pontos = -1
    end
  end

end
