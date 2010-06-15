class Resultado

  attr_accessor "gols_time_a","gols_time_b"
  def initialize(gols_time_a, gols_time_b)
    @gols_time_a = gols_time_a
    @gols_time_b = gols_time_b
  end

  def acertou_gols_time_a(resultado)
    return @gols_time_a == resultado.gols_time_a
  end

  def acertou_gols_time_b(resultado)
    return @gols_time_b == resultado.gols_time_b
  end

  def empate?
    return @gols_time_b == @gols_time_a
  end

  def pontuacao_resultado(resultado_final)
    if acertou_gols_time_a(resultado_final) || acertou_gols_time_b(resultado_final)
      return 1
    end
    if empate? == resultado_final.empate?
      return 2
    end
    return 0
  end

end

def bolao(apostador1, aposta, placar)
  return [apostador1, 0] if aposta[2] != placar[2]
  [apostador1, 1]
end
