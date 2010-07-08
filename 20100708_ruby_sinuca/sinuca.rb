class Jogada

  def initialize(bola_da_vez, bola_alvo, acertou, matou)
    @bola_da_vez = bola_da_vez
    @bola_alvo = bola_alvo
    @acertou = acertou
    @matou = matou
  end

  def pontos

    if @bola_alvo == @bola_da_vez
      if @acertou
        return 0
      else
        return -@bola_da_vez
      end

    else
      if @acertou
        if not @matou
          return -@bola_alvo
        end
      end
    end

  end




end
