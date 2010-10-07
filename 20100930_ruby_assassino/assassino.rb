def assassina(pessoas, passo)

  ordem_das_mortes = (0..pessoas-1).to_a
  lista_pessoas = ordem_das_mortes.dup * passo
  mortos = []
  indice = -1
  while mortos.size < pessoas
    indice += passo
    if not lista_pessoas[indice].morto
      lista_pessoas[indice].morto = true
      mortos << lista_pessoas[indice]
    end
  end
  return mortos

end

class Fixnum

  attr_accessor :morto

end
