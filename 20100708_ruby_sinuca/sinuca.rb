class Jogada

  def initialize(bola_da_vez, bola_alvo, acertou, matou)
    @bola_da_vez = bola_da_vez
    @bola_alvo = bola_alvo
    @acertou = acertou
    @matou = matou
  end

  def pontos
    if @acertou
      0
    else
      -1*@bola_da_vez
    end
  end


end
