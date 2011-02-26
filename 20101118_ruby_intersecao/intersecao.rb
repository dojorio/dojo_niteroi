class Retangulo

  attr_reader 'ponto_1', 'ponto_2'
  def initialize(ponto_1, ponto_2)
    @ponto_1 = ponto_1
    @ponto_2 = ponto_2
  end
  
  def intersecao(retangulo)
   
    return "Não possui interseção" if nao_tem_intersecao(retangulo)
    Retangulo.new(retangulo.ponto_1, @ponto_2)
  end
  
  def nao_tem_intersecao(retangulo)
    return true if (retangulo.ponto_2[0] < @ponto_1[0] or @ponto_2[0] < retangulo.ponto_1[0])
    return true if (retangulo.ponto_2[1] < @ponto_1[1] or @ponto_2[1] < retangulo.ponto_1[1])
  end
    
  def ==(retangulo)
    (@ponto_1 == retangulo.ponto_1 and @ponto_2 == retangulo.ponto_2)
  end
end
