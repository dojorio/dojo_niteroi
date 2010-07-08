class Jogada

  attr_accessor :pontos

  def initialize(bola_da_vez, bola_alvo, acertou, matou)
    @pontos = (0 if acertou else -1)
  end

end
