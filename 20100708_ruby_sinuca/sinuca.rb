class Jogada

  attr_accessor :pontos

  def initialize(bola_da_vez, bola_alvo, acertou, matou)
    @pontos = (if acertou 0 else -1)
  end

end
