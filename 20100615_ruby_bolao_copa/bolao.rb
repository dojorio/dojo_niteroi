class Resultado

  attr_accessor "gols_time_a","gols_time_b"
  def initialize(gols_time_a, gols_time_b)
    @gols_time_a = gols_time_a
    @gols_time_b = gols_time_b
  end

  def pontuacao_resultado(resultado_final)
    if @gols_time_a == resultado_final.gols_time_a
      return 1
    end
    if @gols_time_b == resultado_final.gols_time_b
      return 1
    end
    return 0
  end

end

def bolao(apostador1, aposta, placar)
  return [apostador1, 0] if aposta[2] != placar[2]
  [apostador1, 1]
end
