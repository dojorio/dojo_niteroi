class Jogada

  def initialize(bola_da_vez, bola_alvo, acertou, matou)
    @bola_da_vez = bola_da_vez
    @bola_alvo = bola_alvo
    @acertou = acertou
    @matou = matou
  end

  def pontos




    if @acertou
      if @bola_alvo != @bola_da_vez
        if @matou == false
          -@bola_alvo
        end
      else
        0
      end
    else
      -@bola_da_vez
    end
  end


end
