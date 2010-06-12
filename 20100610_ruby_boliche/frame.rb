class Frame
  SPARE = '/'
  STRIKE = "X"

  def initialize(jogada_1, jogada_2)
    @jogada_1 = jogada_1
    @jogada_2 = jogada_2
  end

  def spare?
    @jogada_2 == SPARE
  end

  def strike?
    @jogada_1 == STRIKE
  end

  def sum
    @jogada_1 + @jogada_2
  end

end
